import os
import re
import glob

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav_m = re.search(r'(<!-- Topbar Start -->.*?</nav>)', text, re.DOTALL)
footer_m = re.search(r'(<!-- Footer Start -->.*?<!-- Copyright End -->)', text, re.DOTALL)
marquee_m = re.search(r'(<div class="premium-marquee-wrapper".*?</div>\s*</div>\s*</div>)', text, re.DOTALL)
root_style_m = re.search(r'<style>\s*:root\s*\{.*?</style>', text, re.DOTALL)

nav_html = nav_m.group(1) if nav_m else ""
footer_html = footer_m.group(1) if footer_m else ""
marquee_html = marquee_m.group(1) if marquee_m else ""
root_style = root_style_m.group(0) if root_style_m else ""

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

files = glob.glob('*.html')
skipped = ['index.html', 'index2.html', 'index3.html', 'index_new.html', 'index_backup.html']

for file in files:
    if file in skipped: continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    orig = content
    
    # Nav replacement
    if nav_html and '<!-- Topbar Start -->' in content:
        # replace up to old </nav>
        content = re.sub(r'<!-- Topbar Start -->.*?</nav>', nav_html.replace('\\', '\\\\'), content, flags=re.DOTALL)
        
    # Footer replacement
    if footer_html and '<!-- Footer Start -->' in content:
        # replace up to Copyright End if present, else just take old Footer End
        content = re.sub(r'<!-- Footer Start -->.*?(<!-- Copyright End -->|<!-- Footer End -->)', footer_html.replace('\\', '\\\\'), content, flags=re.DOTALL)
        
    # Inject root style
    if root_style and ':root' not in content:
        content = content.replace('</head>', f'{root_style}\n  </head>')
        
    if '/* Enforce New Theme Colors Everywhere */' not in content:
        content = content.replace('</head>', f'{override_style}\n  </head>')

    # Convert old breadcrumb header to new hero
    old_header = re.search(r'<!-- Header Start -->.*?<div class="container-fluid bg-breadcrumb.*?<!-- Header End -->', content, re.DOTALL)
    if old_header:
        title_match = re.search(r'<h1.*?>(.*?)</h1>', old_header.group(0), re.DOTALL | re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else file.replace('-',' ').replace('.html', '').title()
        
        new_header = f'''<!-- Modern Hero Start -->
    <div class="new-hero" style="min-height: 450px; height: 50vh; display: flex; align-items: center; justify-content: center; text-align: center; background: linear-gradient(135deg, #FFF3E0 0%, #E8F5E9 100%);">
      <div class="container relative z-index-2">
        <h1 class="hero-title" style="font-size: 3rem; color: var(--text-main); font-weight: 700; text-transform: uppercase;">
          <span style="color: var(--primary);">{title}</span>
        </h1>
      </div>
    </div>
    <!-- Modern Hero End -->'''
        content = content.replace(old_header.group(0), new_header)

    # Some cards are dark e.g., bg-dark, let's just make sure they aren't totally black and replace text-white. 
    # But only if it's the old style, just blindly removing bg-dark and text-white will fix the footer?
    # No, wait, the footer HTML we injected from index.html might have text-light we want.
    # WAIT! The new footer has a specific class: .ultra-footer. 
    
    if content != orig:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated", file)
