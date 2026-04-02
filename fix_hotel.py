import re

with open('hotel-booking.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix cta-box
content = re.sub(
    r'background:\s*radial-gradient\(circle at center,\s*#1a1a1a\s*0%,\s*#050505\s*100%\);',
    r'background: linear-gradient(135deg, var(--bg-light) 0%, #fff 100%);',
    content
)
content = re.sub(
    r'box-shadow:\s*0\s*10px\s*30px\s*rgba\(0,0,0,0\.5\);',
    r'box-shadow: var(--shadow-md);',
    content
)

# And another '#050505' instance?
content = content.replace('#050505', '#ffffff')

with open('hotel-booking.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed hotel-booking.html extra dark styles")
