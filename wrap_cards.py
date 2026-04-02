import sys

with open('taxi-services.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '<div class="d-flex justify-content-between align-items-center mb-3">',
    '<div class="d-flex flex-wrap justify-content-between align-items-center mb-3 gap-2">'
)

with open('taxi-services.html', 'w', encoding='utf-8') as f:
    f.write(text)
