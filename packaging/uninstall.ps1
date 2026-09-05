# ตัวถอนม็อดแปลไทย Judgment (JETH)
# คืนฟอนต์จากไฟล์สำรอง .orig และลบโฟลเดอร์ม็อดออก — ไม่แตะไฟล์อื่นของเกม

$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

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
Write-Host '=== ม็อดแปลไทย Judgment (JETH) — ถอนการติดตั้ง ===' -ForegroundColor Cyan
Write-Host ''

$media = Find-Game
if (-not $media) {
    Write-Host 'หาโฟลเดอร์เกมอัตโนมัติไม่เจอ' -ForegroundColor Yellow
    $inp = (Read-Host 'วางพาธของโฟลเดอร์ที่มี Judgment.exe').Trim('"', ' ')
    if (Test-Path (Join-Path $inp 'Judgment.exe')) { $media = $inp }
    else { Write-Host 'พาธไม่ถูกต้อง — ยกเลิก' -ForegroundColor Red; exit 1 }
}
Write-Host ("พบเกมที่: " + $media)

# คืนเฉพาะสองไฟล์ที่ม็อดนี้เขียนทับ — ไฟล์ .orig อื่นอาจเป็นของม็อดตัวอื่น ห้ามไปยุ่ง
$fontDst = Join-Path $media 'data\font.judge\en'
foreach ($name in @('meta_ot_cond_book.dds', 'meta_ot_cond_book_italic.dds')) {
    $dst = Join-Path $fontDst $name
    $orig = "$dst.orig"
    if (Test-Path $orig) {
        Copy-Item $orig $dst -Force
        Remove-Item $orig
        Write-Host ("  คืนฟอนต์เดิม: " + $name)
    }
}

$modDst = Join-Path $media 'mods\JudgmentThai'
if (Test-Path $modDst) {
    Remove-Item $modDst -Recurse -Force
    Write-Host '  ลบ mods\JudgmentThai'
}

$srmm = Join-Path $media 'ShinRyuModManager.exe'
if (Test-Path $srmm) {
    Push-Location $media
    & $srmm -s | Out-Null
    Pop-Location
    Write-Host '  สร้าง YakuzaParless.mlo ใหม่'
}

Write-Host ''
Write-Host 'ถอนการติดตั้งเรียบร้อย เกมกลับเป็นภาษาอังกฤษตามเดิม' -ForegroundColor Green
Write-Host 'หมายเหตุ: ไฟล์ตัวโหลดม็อด (ShinRyuModManager.exe / version.dll / YakuzaParless.asi)'
Write-Host 'ไม่ได้ถูกลบ เพราะม็อดตัวอื่นอาจใช้อยู่ — ลบเองได้ถ้าไม่ใช้แล้ว'
Write-Host ''
