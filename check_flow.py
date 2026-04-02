import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's extract the main layout containers/sections
pattern = r'<(div|section)[^>]*class=[\'\"]([^\'\"]*)[\'\"][^>]*>'
matches = re.finditer(pattern, html)

print("--- Flow of main sections in index.html ---")
skip_inner = ['col-', 'row', 'card', 'd-flex', 'nav', 'collapse', 'navbar', 'btn']

for m in matches:
    cls = m.group(2)
    if any(x in cls for x in ['container', 'hero', 'section', 'bg-', 'py-', 'pt-', 'features', 'testimonial']):
        if not any(x in cls for x in skip_inner):
            print(f"- {cls[:80]}")
