import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

with open('about.html', 'r', encoding='utf-8') as f:
    abt = f.read()

# 1. Grab everything before </head> in index.html (except the actual <title> and meta which should stay specific)
# Let's extract the styles exactly.
idx_styles = ""
style_match = re.search(r'(<style>.*?</style>\s*<style>.*?</style>)', idx, re.DOTALL)
if style_match:
    idx_styles = style_match.group(1)

# Ensure the new fonts are there
font_links = """    <!-- Google Web Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&amp;family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&amp;display=swap" rel="stylesheet">"""

# Replace about fonts
abt = re.sub(r'<!-- Google Fonts -->.*?rel="stylesheet">', font_links, abt, flags=re.DOTALL)

# Replace the style block in about.html
abt = re.sub(r'<style>.*?</style>', idx_styles, abt, count=1, flags=re.DOTALL)

# 2. Grab the new-nav from index
nav_match = re.search(r'(<!-- Elegant Nav -->\s*<nav.*?</nav>)', idx, re.DOTALL)
if nav_match:
    idx_nav = nav_match.group(1)
    # Replace anything between <body> and the hero section in about
    abt = re.sub(r'<body.*?(<section)', '<body>\n\n' + idx_nav + '\n\n\\1', abt, flags=re.DOTALL, count=1)
    
    # Actually about.html doesn't have a nav right now in the read snippet ? Wait, it probably does but maybe it's in a separate file or not included in my regex. Let me just replace the existing nav or insert it.
    if '<nav' in abt and '<!-- Elegant Nav -->' not in abt:
        abt = re.sub(r'<nav.*?</nav>', idx_nav, abt, flags=re.DOTALL, count=1)

# 3. Replace Footer
footer_match = re.search(r'(<style>\s*/\* Modern Luxurious Footer \*/.*?)<!-- Floating Call', idx, re.DOTALL)
if footer_match:
    idx_footer = footer_match.group(1)
    # in about.html, replace from <!-- Footer Start --> to <!-- Floating
    abt = re.sub(r'<!-- Footer Start -->.*?(?=<!-- Floating Call)', '<!-- Footer Start -->\n' + idx_footer, abt, flags=re.DOTALL)

# 4. Hero section class update
# The about-hero section:
# <div class="about-hero">...</div> or <section class="about-hero">
abt = re.sub(r'class="about-hero"', 'class="new-hero"', abt)
abt = re.sub(r'class="about-section"', 'class="booking-widget"', abt)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(abt)

print("Format copied to about.html")
