import re

with open('c:/data/newc/about/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

with open('c:/data/newc/about/service.html', 'r', encoding='utf-8') as f:
    service_content = f.read()

def get_style(pattern, content):
    m = re.search(pattern, content, re.DOTALL)
    if m: return m.group(0)
    return ""

root_style = get_style(r'<style>\s*:root\s*\{.*?</style>', index_content)
marquee_style = get_style(r'<style>\s*\.premium-marquee-wrapper\s*\{.*?</style>', index_content)
footer_style = get_style(r'<style>\s*/\*\s*Modern Luxurious Footer\s*\*/.*?</style>', index_content)

# 1. Inject root style into head if missing
if root_style and ':root' not in get_style(r'<head>.*?</head>', service_content):
    service_content = service_content.replace('</head>', f'{root_style}\n  </head>')

# 2. Replace Marquis Style
old_marquee = get_style(r'<style>\s*\.premium-marquee-wrapper\s*\{.*?</style>', service_content)
if old_marquee and marquee_style:
    service_content = service_content.replace(old_marquee, marquee_style)

# 3. Replace Footer Style
old_footer = get_style(r'<style>\s*/\*\s*Modern Luxurious Footer\s*\*/.*?</style>', service_content)
if old_footer and footer_style:
    service_content = service_content.replace(old_footer, footer_style)

with open('c:/data/newc/about/service_new.html', 'w', encoding='utf-8') as f:
    f.write(service_content)

print("Done generating service_new.html")
