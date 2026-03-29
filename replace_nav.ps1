$file = "c:\data\newc\about\index3.html"
$content = Get-Content $file -Raw
$navContent = Get-Content "c:\data\newc\about\new_nav.txt" -Raw

$startTag = "<!-- Sticky Navbar & Hero Start -->"
$endTag = "<!-- New Age Cinematic Hero -->"

$escStart = [regex]::Escape($startTag)
$escEnd = [regex]::Escape($endTag)

$pattern = "(?s)$escStart.*?$escEnd"

if ($content -match $pattern) {
    $newText = "$startTag`n$navContent`n  $endTag"
    $newContent = $content -replace $pattern, $newText
    Set-Content $file $newContent -Encoding UTF8
    Write-Host "SUCCESS: Navigation was upgraded!"
} else {
    Write-Host "ERROR: Could not find the replacement pattern!"
}
