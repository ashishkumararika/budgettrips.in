import sys
text = open('index.html', encoding='utf-8').read()

import re
print("Padding fixed:")
print(len(re.findall(r'padding:\s*[0-9]+px', text)))

print("d-flex without wrap:")
for m in re.findall(r'<div[^>]*class="[^"]*d-flex[^"]*"[^>]*>', text):
    if 'flex-wrap' not in m and 'nav' not in m and 'column' not in m:
        print(m[:80])

