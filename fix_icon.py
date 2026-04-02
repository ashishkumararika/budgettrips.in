import sys
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('fa-steering-wheel', 'fa-route')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
