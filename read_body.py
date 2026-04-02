import re

with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

body_match = re.search(r'<body.*?>(.*)</body>', text, re.DOTALL)
if body_match:
    with open('body.txt', 'w', encoding='utf-8') as b:
        b.write(body_match.group(1))
