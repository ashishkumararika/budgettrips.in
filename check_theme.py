import re

with open('c:/data/newc/about/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

with open('c:/data/newc/about/service.html', 'r', encoding='utf-8') as f:
    service_content = f.read()

root_style_match = re.search(r'<style>\s*:root\s*\{.*?</style>', index_content, re.DOTALL)
if root_style_match:
    print('Found root style in index.html, length:', len(root_style_match.group(0)))

dark_classes = set(re.findall(r'class="[^"]*dark[^"]*"', service_content))
print('Dark classes:', dark_classes)

bg_dark = set(re.findall(r'bg-dark', service_content))
print('bg-dark found:', bool(bg_dark))
text_light = set(re.findall(r'text-light', service_content))
print('text-light found:', bool(text_light))
