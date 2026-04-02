import re

with open('c:/data/newc/about/service_new.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find footer section
match = re.search(r'(<!-- Footer Start -->.*?<!-- Footer End -->)', text, re.DOTALL)
if match:
    footer = match.group(1)
    new_footer = footer.replace('text-white', 'text-dark')
    text = text.replace(footer, new_footer)

with open('c:/data/newc/about/service_new.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed text-white in footer")
