import sys

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the media query block we just injected to include .hero-title
old_css = '''/* Global Mobile Responsiveness Fixes */
@media (max-width: 768px) {
    .display-4 { font-size: 2.5rem !important; }'''

new_css = '''/* Global Mobile Responsiveness Fixes */
@media (max-width: 768px) {
    .hero-title { font-size: 2.8rem !important; }
    .display-4 { font-size: 2.5rem !important; }'''

if old_css in text:
    text = text.replace(old_css, new_css)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed hero title scaling on index.html")

# Do the same for taxi-services.html just in case (optional, we used inline display classes there but just to be thorough)
with open('taxi-services.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

if old_css in text2:
    text2 = text2.replace(old_css, new_css)
    with open('taxi-services.html', 'w', encoding='utf-8') as f:
        f.write(text2)
    print("Fixed hero title scaling on taxi-services.html")
