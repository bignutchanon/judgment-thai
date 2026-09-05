#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""หา **ตาราง width ของฟอนต์ใน RAM ของเกมที่กำลังรัน** แล้วแก้ค่า advance ให้พอดีกับกลิฟไทย

ทำไมต้องแก้ในหน่วยความจำ ไม่แก้ไฟล์:
  * ตาราง advance ไม่ได้อยู่ในไฟล์ dds/bin ของฟอนต์เลย (ตรวจครบแล้ว รวม gothic/symbol.bin)
  * สแกนหาในไฟล์ `Judgment.exe` ด้วยลายเซ็นค่าที่วัดมา 202 ตัวก็ยังไม่เจอ (ข้อมูลถูกบีบ/เข้ารหัส
    ในไฟล์ แต่ตอนรันจะถูกคลายลง RAM) — โมเดลเดียวกับที่ม็อดฝั่ง Yakuza ใช้ hook ตอนรัน
  * แก้ได้แล้วจะปลดล็อกสองเรื่องพร้อมกัน:
      - ตั้ง advance ของ **มาร์ก** (สระบน/วรรณยุกต์) = 0 -> ซ้อนบนฐานได้จริง ไม่ต้อง pre-compose
      - ตั้ง advance ของ **ฐาน** = ความกว้างกลิฟ + ช่องไฟ -> ตัวอักษรชิดกันเป็นธรรมชาติ
    (เซลล์ว่างของ Latin Ext-A ทุกช่องตอนนี้ advance ตายตัว 36 px ซึ่งกว้างกว่ากลิฟไทย 12-20 px)

ปลอดภัย: เขียนเฉพาะ "ช่องความกว้างของ codepoint ที่ม็อดยึดไปใช้" เท่านั้น ไม่แตะโค้ด ไม่แตะไฟล์เกม
ผลจะหายเมื่อปิดเกม (ต้องรันซ้ำทุกครั้งที่เปิดเกม จนกว่าจะทำเป็น .asi)

ใช้ (ต้องเปิดเกมค้างไว้ที่หน้าไตเติล):
  python scripts/patch_widths_mem.py --scan            # หาตาราง แล้วรายงานที่อยู่ที่เจอ
  python scripts/patch_widths_mem.py --apply           # หา + เขียนค่าใหม่จาก slotmap
  python scripts/patch_widths_mem.py --apply --addr 0x7FF6xxxxxxx   # ระบุที่อยู่ตรง ๆ
"""
import argparse
import ctypes
import ctypes.wintypes as wt
import io
import json
import sys
from pathlib import Path

import numpy as np

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths                                    # noqa: E402

PROC_NAME = "Judgment.exe"
WIDTHS = paths.TRANSLATIONS / "donor_widths.json"

PROCESS_ALL = 0x1F0FFF
MEM_COMMIT = 0x1000
PAGE_GUARD = 0x100
READABLE = (0x02, 0x04, 0x20, 0x40, 0x80)       # R, RW, XR, XRW, XWC

k32 = ctypes.WinDLL("kernel32", use_last_error=True)
psapi = ctypes.WinDLL("psapi", use_last_error=True)


class MEMORY_BASIC_INFORMATION64(ctypes.Structure):
    _fields_ = [("BaseAddress", ctypes.c_ulonglong),
                ("AllocationBase", ctypes.c_ulonglong),
                ("AllocationProtect", wt.DWORD),
                ("__alignment1", wt.DWORD),
                ("RegionSize", ctypes.c_ulonglong),
                ("State", wt.DWORD),
                ("Protect", wt.DWORD),
                ("Type", wt.DWORD),
                ("__alignment2", wt.DWORD)]


def find_pid(name=PROC_NAME):
    arr = (wt.DWORD * 4096)()
    got = wt.DWORD()
    psapi.EnumProcesses(ctypes.byref(arr), ctypes.sizeof(arr), ctypes.byref(got))
    for i in range(got.value // ctypes.sizeof(wt.DWORD)):
        pid = arr[i]
        h = k32.OpenProcess(0x1000, False, pid)         # QUERY_LIMITED_INFORMATION
        if not h:
            continue
        buf = ctypes.create_unicode_buffer(512)
        size = wt.DWORD(512)
        ok = k32.QueryFullProcessImageNameW(h, 0, buf, ctypes.byref(size))
        k32.CloseHandle(h)
        if ok and buf.value.lower().endswith(name.lower()):
            return pid, buf.value
    return None, None


def regions(h):
    """ช่วงหน่วยความจำที่อ่านได้ของโปรเซส"""
    mbi = MEMORY_BASIC_INFORMATION64()
    addr = 0
    out = []
    while k32.VirtualQueryEx(h, ctypes.c_void_p(addr), ctypes.byref(mbi), ctypes.sizeof(mbi)):
        if (mbi.State == MEM_COMMIT and (mbi.Protect & 0xFF) in READABLE
                and not (mbi.Protect & PAGE_GUARD)):
            out.append((mbi.BaseAddress, mbi.RegionSize))
        addr = mbi.BaseAddress + mbi.RegionSize
        if addr > 0x7FFFFFFFFFFF:
            break
    return out


def read(h, addr, size):
    buf = (ctypes.c_ubyte * size)()
    got = ctypes.c_size_t()
    if not k32.ReadProcessMemory(h, ctypes.c_void_p(addr), ctypes.byref(buf), size,
                                 ctypes.byref(got)):
        return None
    return np.frombuffer(bytes(buf[:got.value]), dtype=np.uint8)


def write(h, addr, data):
    buf = (ctypes.c_ubyte * len(data))(*data)
    put = ctypes.c_size_t()
    old = wt.DWORD()
    k32.VirtualProtectEx(h, ctypes.c_void_p(addr), len(data), 0x40, ctypes.byref(old))
    ok = k32.WriteProcessMemory(h, ctypes.c_void_p(addr), ctypes.byref(buf), len(data),
                                ctypes.byref(put))
    k32.VirtualProtectEx(h, ctypes.c_void_p(addr), len(data), old, ctypes.byref(old))
    return bool(ok) and put.value == len(data)


def signature():
    """(ดัชนี, ค่าที่วัดได้) ของ donor ทั้ง 202 ตัว — ลายเซ็นที่ใช้ค้นในหน่วยความจำ

    ดัชนีลองสองแบบ: ตาม codepoint ตรง ๆ และตามเลขเซลล์ใน atlas (cp>=0xA0 -> cp-0x20)
    """
    w = json.load(io.open(WIDTHS, encoding="utf-8"))["widths"]
    meas = {int(k, 16): v for k, v in w.items()}
    by_cp = sorted(meas.items())
    by_cell = sorted(((cp if cp < 0x80 else cp - 0x20), v) for cp, v in meas.items())
    return {"cp": by_cp, "cell": by_cell}


def scan_block(block, idx_vals, kind, stride, min_corr=0.97):
    """หา offset ในบล็อกที่ค่าตรงกับลายเซ็น -> [(offset, corr)]"""
    idxs = np.array([i for i, _ in idx_vals], dtype=np.int64) * stride
    vals = np.array([v for _, v in idx_vals], dtype=np.float64)
    span = int(idxs.max()) + 8
    n = len(block) - span
    if n <= 0:
        return []

    def col(off_idx):
        o = int(idxs[off_idx])
        if kind == "u8":
            return block[o:o + n].astype(np.float32)
        if kind == "u16":
            v = block[o:o + n + 1]
            return v[:n].astype(np.float32) + v[1:n + 1].astype(np.float32) * 256.0
        b = [block[o + k:o + k + n].astype(np.uint32) << (8 * k) for k in range(4)]
        return (b[0] | b[1] | b[2] | b[3]).view(np.float32)

    # กรองหยาบให้เร็วที่สุดก่อน: ค่าที่วัดได้มีกลุ่มใหญ่ที่ "เท่ากันเป๊ะ" (เซลล์ว่าง Ext-A = 36 px
    # ทั้ง 128 ช่อง) -> ตำแหน่งที่ใช่ต้องมีค่าเท่ากันทุกช่องในกลุ่มนั้น เป็นตัวกรองที่คมและถูกมาก
    from collections import Counter
    common = Counter(vals.tolist()).most_common(1)[0][0]
    same = [i for i, v in enumerate(vals) if v == common][:8]
    keep = np.ones(n, dtype=bool)
    if len(same) >= 3:
        ref = col(same[0])
        for i in same[1:]:
            keep &= ref == col(i)
            if not keep.any():
                return []
    order = np.argsort(vals)
    probe = [order[0], order[len(order) // 3], order[2 * len(order) // 3], order[-1]]
    for a, b in zip(probe, probe[1:]):
        keep &= col(a) < col(b)
        if not keep.any():
            return []
    cand = np.flatnonzero(keep)
    if not len(cand):
        return []
    vc = vals - vals.mean()
    vn = np.sqrt((vc ** 2).sum())
    out = []
    for i0 in range(0, len(cand), 50000):
        blk = cand[i0:i0 + 50000]
        M = np.stack([col(i)[blk] for i in range(len(idxs))], axis=1).astype(np.float64)
        ok = np.isfinite(M).all(axis=1) & (M.std(axis=1) > 0)
        M, b2 = M[ok], blk[ok]
        if not len(b2):
            continue
        mc = M - M.mean(axis=1, keepdims=True)
        corr = (mc * vc).sum(axis=1) / (np.sqrt((mc ** 2).sum(axis=1)) * vn)
        for h in np.flatnonzero(corr >= min_corr):
            out.append((int(b2[h]), float(corr[h])))
    return out


def scan(h, sigs, kinds=("u8", "u16", "f32"), verbose=True):
    hits = []
    regs = regions(h)
    total = sum(r[1] for r in regs)
    if verbose:
        print("ช่วงหน่วยความจำที่อ่านได้ %d ช่วง รวม %.1f GB" % (len(regs), total / 1e9))
    done = 0
    for base, size in regs:
        step = 8 << 20
        for off in range(0, size, step):
            chunk = min(step + 4096, size - off)
            blk = read(h, base + off, chunk)
            done += chunk
            if blk is None or len(blk) < 1024:
                continue
            for name, idx_vals in sigs.items():
                for kind in kinds:
                    for stride in ((1, 2, 4) if kind == "u8" else (2, 4) if kind == "u16" else (4, 8)):
                        for pos, corr in scan_block(blk, idx_vals, kind, stride):
                            addr = base + off + pos
                            hits.append((addr, name, kind, stride, corr))
                            if verbose:
                                print("  พบ 0x%X (%s/%s stride %d) corr %.4f"
                                      % (addr, name, kind, stride, corr))
        if verbose and total:
            pass
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--addr", default="", help="ที่อยู่ตารางที่รู้แล้ว (เลขฐานสิบหก)")
    ap.add_argument("--kinds", default="u8")
    a = ap.parse_args()

    pid, path = find_pid()
    if not pid:
        sys.exit("!! ไม่พบโปรเซส %s — เปิดเกมค้างไว้ที่หน้าไตเติลก่อน" % PROC_NAME)
    print("เจอเกม pid=%d (%s)" % (pid, path))
    h = k32.OpenProcess(PROCESS_ALL, False, pid)
    if not h:
        sys.exit("!! เปิดโปรเซสไม่ได้ (ลองรัน terminal แบบ Run as administrator)")

    sigs = signature()
    if a.addr:
        addr = int(a.addr, 16)
        blk = read(h, addr, 1024)
        print("ค่าที่ 0x%X: %s" % (addr, list(blk[:64])))
        return 0

    hits = scan(h, sigs, tuple(k.strip() for k in a.kinds.split(",")))
    print("เจอผู้สมัคร %d จุด" % len(hits))
    if not hits:
        print("ไม่เจอ — ลอง --kinds u8,u16,f32 หรือเปิดเกมให้ถึงหน้าที่มีข้อความไทยก่อนสแกน")
    return 0


if __name__ == "__main__":
    sys.exit(main())
