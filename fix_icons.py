import re

with open('c:/data/newc/about/service_retheme.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the broken div from the first replacement
text = text.replace(
'''<div class="bento-icon me-4" style="margin-bottom: 0;"><i class="fas fa-taxi"></i></div>
                </div>''', 
'''<div class="bento-icon me-4" style="margin-bottom: 0;"><i class="fas fa-taxi"></i></div>'''
)

# Fix the other icons to use bento-icon
def replace_bento_icon(match):
    icon_class = match.group(1)
    return f'<div class="bento-icon me-4" style="margin-bottom: 0;"><i class="{icon_class}"></i></div>'

text = re.sub(r'<div class="me-4">\s*<i class="([^"]+) fa-4x [^"]+"></i>\s*</div>', replace_bento_icon, text)

# There is a remaining text-muted we can touch up inside the header if it exists
with open('c:/data/newc/about/service_retheme.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed bento icons.")
