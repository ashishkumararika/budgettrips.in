import re

with open('c:/data/newc/about/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

with open('c:/data/newc/about/service.html', 'r', encoding='utf-8') as f:
    service_content = f.read()

def get_style(pattern, content):
    m = re.search(pattern, content, re.DOTALL)
    if m: return m.group(0)
    return ""

nav_style = get_style(r'<style>\s*/\*\s*Ultra Modern Glassmorphism Navbar CSS\s*\*/.*?</style>', index_content)
old_nav_style = get_style(r'<style>\s*/\*\s*Ultra Modern Glassmorphism Navbar CSS\s*\*/.*?</style>', service_content)

if old_nav_style and nav_style:
    service_content = service_content.replace(old_nav_style, nav_style)
    # also change hardcoded #003A66 text in the nav logo
    service_content = service_content.replace('#003A66', 'var(--text-main)')
    with open('c:/data/newc/about/service.html', 'w', encoding='utf-8') as f:
        f.write(service_content)
    print("Updated navbar styles")
