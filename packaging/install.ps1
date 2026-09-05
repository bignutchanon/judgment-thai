# ตัวติดตั้งม็อดแปลไทย Judgment (JETH)
# ติดตั้งด้วยวิธีที่ทดสอบแล้วว่าใช้ได้จริง:
#   * ข้อความ -> โฟลเดอร์ mods (Parless โหลดให้)
#   * ฟอนต์   -> เขียนทับไฟล์ในเกมตรง ๆ พร้อมสำรองเป็น .orig ก่อนเสมอ
#     (ฟอนต์โหลดตั้งแต่ก่อน Parless จะ hook จึงวางในโฟลเดอร์ mods ไม่ได้)

$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$files = Join-Path $root 'files'

function Find-Game {
    $cands = @()
    $steam = (Get-ItemProperty 'HKCU:\Software\Valve\Steam' -ErrorAction SilentlyContinue).SteamPath
    if ($steam) {
        $cands += $steam
        $vdf = Join-Path $steam 'steamapps\libraryfolders.vdf'
        if (Test-Path $vdf) {
            foreach ($m in (Select-String -Path $vdf -Pattern '"path"\s*"(.+?)"' -AllMatches).Matches) {
                $cands += $m.Groups[1].Value -replace '\\\\', '\'
            }
        }
    }
    $cands += 'C:\Program Files (x86)\Steam'
    foreach ($c in $cands) {
        $p = Join-Path $c 'steamapps\common\Judgment\runtime\media'
        if (Test-Path (Join-Path $p 'Judgment.exe')) { return $p }
    }
    return $null
}

Write-Host ''
Write-Host '=== ม็อดแปลไทย Judgment (JETH) — ตัวติดตั้ง ===' -ForegroundColor Cyan
Write-Host ''

$media = Find-Game
if (-not $media) {
    Write-Host 'หาโฟลเดอร์เกมอัตโนมัติไม่เจอ' -ForegroundColor Yellow
    Write-Host 'ให้วางพาธของโฟลเดอร์ที่มีไฟล์ Judgment.exe (…\Judgment\runtime\media)'
    $inp = (Read-Host 'พาธ').Trim('"', ' ')
    if (Test-Path (Join-Path $inp 'Judgment.exe')) { $media = $inp }
    else { Write-Host 'พาธไม่ถูกต้อง — ยกเลิก' -ForegroundColor Red; exit 1 }
}
Write-Host ("พบเกมที่: " + $media)

# ---- 1) ฟอนต์: สำรอง .orig ครั้งแรก แล้วเขียนทับ ----
$fontDst = Join-Path $media 'data\font.judge\en'
if (-not (Test-Path $fontDst)) { Write-Host 'ไม่พบโฟลเดอร์ฟอนต์ของเกม — ยกเลิก' -ForegroundColor Red; exit 1 }
foreach ($f in Get-ChildItem (Join-Path $files 'font') -Filter *.dds) {
    $dst = Join-Path $fontDst $f.Name
    $orig = "$dst.orig"
    if ((Test-Path $dst) -and -not (Test-Path $orig)) {
        Copy-Item $dst $orig
        Write-Host ("  สำรองไฟล์เดิม: " + $f.Name + '.orig')
    }
    Copy-Item $f.FullName $dst -Force
    Write-Host ("  ติดตั้งฟอนต์: " + $f.Name)
}

# ---- 2) ข้อความ: โฟลเดอร์ mods ----
$modDst = Join-Path $media 'mods\JudgmentThai'
if (Test-Path $modDst) { Remove-Item $modDst -Recurse -Force }
New-Item -ItemType Directory -Force -Path (Split-Path $modDst) | Out-Null
Copy-Item (Join-Path $files 'JudgmentThai') $modDst -Recurse
$n = (Get-ChildItem $modDst -Recurse -File).Count
Write-Host ("  ติดตั้งข้อความ: mods\JudgmentThai (" + $n + ' ไฟล์)')

# ---- 3) ตัวโหลดม็อด (ใส่ให้เฉพาะที่ยังไม่มี) ----
foreach ($f in Get-ChildItem (Join-Path $files 'loader') -File) {
    $dst = Join-Path $media $f.Name
    if (-not (Test-Path $dst)) {
        Copy-Item $f.FullName $dst
        Write-Host ("  ติดตั้งตัวโหลดม็อด: " + $f.Name)
    } else {
        Write-Host ("  มีตัวโหลดม็อดอยู่แล้ว: " + $f.Name)
    }
}

# ---- 4) สร้างรายการไฟล์ให้ Parless ----
$srmm = Join-Path $media 'ShinRyuModManager.exe'
if (Test-Path $srmm) {
    Push-Location $media
    & $srmm -s | Out-Null
    Pop-Location
    $mlo = Join-Path $media 'YakuzaParless.mlo'
    if (Test-Path $mlo) { Write-Host '  สร้าง YakuzaParless.mlo สำเร็จ' }
    else { Write-Host '  !! สร้าง YakuzaParless.mlo ไม่สำเร็จ' -ForegroundColor Red }
}

Write-Host ''
Write-Host 'ติดตั้งเสร็จแล้ว' -ForegroundColor Green
Write-Host 'เข้าเกมแล้วตั้งภาษาข้อความเป็น English (ม็อดแทนที่ข้อความชุดอังกฤษ)'
Write-Host 'ถอนการติดตั้งด้วย uninstall.bat'
Write-Host ''
