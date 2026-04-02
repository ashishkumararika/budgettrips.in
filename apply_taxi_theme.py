import re

with open('c:/data/newc/about/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

with open('c:/data/newc/about/taxi-services.html', 'r', encoding='utf-8') as f:
    target_content = f.read()

def get_style(pattern, content):
    m = re.search(pattern, content, re.DOTALL)
    if m: return m.group(0)
    return ""

root_style = get_style(r'<style>\s*:root\s*\{.*?</style>', index_content)

# 1. Inject root style into head if missing
if root_style and ':root' not in get_style(r'<head>.*?</head>', target_content):
    target_content = target_content.replace('</head>', f'{root_style}\n  </head>')

# Ensure theme colors override
if '/* Enforce New Theme Colors Everywhere */' not in target_content:
    override_style = '''
    <style>
      /* Enforce New Theme Colors Everywhere */
      :root {
        --bs-primary: #FF5E00;
        --bs-primary-rgb: 255, 94, 0;
      }
      .text-primary { color: var(--primary) !important; }
      .bg-primary { background-color: var(--primary) !important; }
      #spinner .text-secondary { color: var(--primary) !important;}
      .btn-primary { 
        background-color: var(--primary) !important; 
        border-color: var(--primary) !important;
        color: white !important;
      }
      .btn-primary:hover {
        background-color: #E85D04 !important;
        border-color: #E85D04 !important;
      }
    </style>
'''
    target_content = re.sub(r'(</head>)', override_style + r'\n  \1', target_content, flags=re.IGNORECASE)

# 2. Modernize the header Hero
old_header = re.search(r'<!-- Header Start -->.*?<!-- Header End -->', target_content, re.DOTALL)
if old_header:
    new_header = '''<!-- Taxi Services Hero Start -->
    <div class="new-hero" style="min-height: 450px; height: 50vh; display: flex; align-items: center; justify-content: center; text-align: center; background: linear-gradient(135deg, #FFF3E0 0%, #E8F5E9 100%);">
      <div class="container relative z-index-2">
        <h1 class="hero-title" style="font-size: 4rem; color: var(--text-main);">Premium <span style="color: var(--primary);">Taxi Services</span></h1>
        <p class="hero-subtitle mx-auto" style="font-size: 1.25rem; color: var(--text-muted); max-width: 700px;">
          Explore Amritsar and North India traversing in our immaculate, luxury-tier vehicles. Driven by professionals, maintained to perfection.
        </p>
      </div>
    </div>
    <!-- Taxi Services Hero End -->'''
    target_content = target_content.replace(old_header.group(0), new_header)

# Make sure footer has the right styles
target_content = target_content.replace('#3b82f6', 'var(--primary)')
target_content = target_content.replace('text-white', 'text-dark')

with open('c:/data/newc/about/taxi-services.html', 'w', encoding='utf-8') as f:
    f.write(target_content)

print("Applied theme structures to taxi-services.html")
