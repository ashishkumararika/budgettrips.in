import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the hero section match the new-hero from index.html
html = re.sub(r'<section class="about-luxury-hero">', '<section class="new-hero" style="min-height: auto; padding: 120px 0 80px 0; border-radius: 0 0 40px 40px;">', html)

# Replace dark backgrounds and texts
html = html.replace('background: #000;', 'background: var(--bg-light);')
html = html.replace('background: #050505;', 'background: var(--bg-light);')
html = html.replace('background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);', '')
html = html.replace('background: linear-gradient(180deg, #000 0%, #0a0a0a 100%);', 'background: white;')

# Replace Gold/Luxury colors with Primary/Secondary
html = html.replace('#d4af37', 'var(--primary)')
html = html.replace('#f9d423', 'var(--accent)')
html = html.replace('#ff4e50', 'var(--secondary)')
html = html.replace('rgba(212, 175, 55,', 'rgba(255, 94, 0,')

# Replace white text with dark text
html = html.replace('color: #fff;', 'color: var(--text-main);')
html = html.replace('color: #a0a0a0;', 'color: var(--text-muted);')
html = html.replace('color: #dfdfdf;', 'color: var(--text-muted);')

# Update Quote Box
html = html.replace('class="luxury-quote-box"', 'class="luxury-quote-box bg-white shadow-sm"')
html = html.replace('border: 1px solid rgba(255, 94, 0, 0.2);', 'border: 1px solid var(--primary);')

# Title gradient removal -> unified text-main
html = re.sub(r'background: linear-gradient.*?;\s*-webkit-background-clip: text;\s*-webkit-text-fill-color: transparent;', 'color: var(--text-main);', html)
html = html.replace('class="about-title"', 'class="hero-title" style="text-align: left; font-size: 4rem;"')

# Ensure text black gets correctly assigned
html = html.replace('color: #000;', 'color: white;') # the button text was black on gold, now white on primary

# Glass boxes -> White cards
html = html.replace('background: rgba(255, 255, 255, 0.03);', 'background: white;')
html = html.replace('border: 1px solid rgba(255, 255, 255, 0.05);', 'border: none; box-shadow: 0 10px 30px rgba(0,0,0,0.05);')
html = html.replace('class="glass-title"', 'class="glass-title text-dark"')

# Reviews card
html = html.replace('background: rgba(20, 20, 20, 0.8);', 'background: white; box-shadow: 0 10px 30px rgba(0,0,0,0.05);')
html = html.replace('border: 1px solid rgba(255, 94, 0, 0.1);', 'border: none;')
html = html.replace('class="review-author"', 'class="review-author text-dark"')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Theme updated!")
