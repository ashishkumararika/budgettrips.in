import re

with open('c:/data/newc/about/service.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the Page Header breadcrumb with a modern hero
old_header = re.search(r'<!-- Services Header Start -->.*?<!-- Services Header End -->', text, re.DOTALL)
if old_header:
    new_header = '''<!-- Services Banner Start -->
    <div class="new-hero" style="min-height: 450px; height: 50vh; display: flex; align-items: center; justify-content: center; text-align: center;">
      <div class="container relative z-index-2">
        <h1 class="hero-title" style="font-size: 4rem; color: var(--text-main);">Our <span style="color: var(--primary);">Premium Services</span></h1>
        <p class="hero-subtitle mx-auto" style="font-size: 1.25rem; color: var(--text-muted); max-width: 600px;">
          Elevating travel across North India from a mere commute into a masterclass in comfort, reliability, and luxury.
        </p>
      </div>
    </div>
    <!-- Services Banner End -->'''
    text = text.replace(old_header.group(0), new_header)

# Modernize the "Explore Our Premium Travel Services" title
text = text.replace('<h2 class="text-primary fw-bold">', '<h2 class="display-4 fw-bold mb-3" style="color: var(--text-main); letter-spacing: -1px;">')

# Let's run a script to add bento-item classes or style the service cards properly
# The service cards currently look like: 
# <div class="p-5 bg-white border shadow-lg rounded-4 h-100 hover-effect d-flex align-items-center">
text = text.replace('class="p-5 bg-white border shadow-lg rounded-4 h-100 hover-effect d-flex align-items-center"', 
                    'class="bento-item h-100 d-flex align-items-center flex-row text-start" style="padding: 2.5rem; justify-content: flex-start;"')

# Increase icon sizes and colors
text = re.sub(r'<i class="([^"]+) fa-4x text-primary"></i>', r'<div class="bento-icon me-4" style="margin-bottom: 0;"><i class="\1"></i></div>', text)
text = re.sub(r'<div class="me-4">\s*<div class="bento-icon me-4"', r'<div class="bento-icon me-4"', text)

# Text overrides
text = text.replace('<h3 class="text-dark">', '<h3 style="font-size: 1.5rem; color: var(--text-main);">')
text = text.replace('<p class="text-muted mb-0">', '<p style="color: var(--text-muted); margin: 0; line-height: 1.6;">')

with open('c:/data/newc/about/service_retheme.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Rethemed service.html to service_retheme.html")
