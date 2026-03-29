$file = "c:\data\newc\about\index3.html"
$content = Get-Content $file -Raw
$navContent = Get-Content "c:\data\newc\about\new_nav_full.txt" -Raw

$startTag = "<!-- Ultra Modern Floating Navbar Start -->"
$endTag = "<!-- Ultra Modern Floating Navbar End -->"

$escStart = [regex]::Escape($startTag)
$escEnd = [regex]::Escape($endTag)

$pattern = "(?s)$escStart.*?$escEnd"

if ($content -match $pattern) {
    $newContent = $content -replace $pattern, $navContent
    Set-Content $file $newContent -Encoding UTF8
    Write-Host "SUCCESS: Navigation was upgraded!"
} else {
    Write-Host "ERROR: Could not find the replacement pattern!"
}
