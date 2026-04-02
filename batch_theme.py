import re
import glob
import os

folder = 'c:/data/newc/about/'

with open(os.path.join(folder, 'index.html'), 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract components from index.html
nav_match = re.search(r'(<!-- Topbar Start -->.*?<!-- Navbar End -->)', index_content, re.DOTALL)
footer_match = re.search(r'(<!-- Footer Start -->.*?<!-- Footer End -->)', index_content, re.DOTALL)
marquee_match = re.search(r'(<div class="scrolling-ticker".*?</div>\s*</div>)', index_content, re.DOTALL)
root_style = re.search(r'<style>\s*:root\s*\{.*?</style>', index_content, re.DOTALL)

if not nav_match or not footer_match:
    print("Could not find nav or footer in index.html")
    exit(1)

nav_html = nav_match.group(1)
footer_html = footer_match.group(1)
root_style_html = root_style.group(0) if root_style else ""

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

html_files = glob.glob(os.path.join(folder, '*.html'))
skipped = ['index', 'index2', 'index3', 'index_new', 'index_backup']

for file in html_files:
    basename = os.path.basename(file)
    name_without_ext = os.path.splitext(basename)[0]
    if name_without_ext in skipped:
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # Replace Nav
    content = re.sub(r'<!-- Topbar Start -->.*?<!-- Navbar End -->', nav_html.replace('\\', '\\\\'), content, flags=re.DOTALL)
    
    # Replace Footer
    content = re.sub(r'<!-- Footer Start -->.*?<!-- Footer End -->', footer_html.replace('\\', '\\\\'), content, flags=re.DOTALL)
    
    # Inject root style if missing
    if ':root' not in re.search(r'<head>.*?</head>', content, re.DOTALL).group(0):
        content = content.replace('</head>', f'{root_style_html}\\n  </head>')
        
    # Inject override
    if '/* Enforce New Theme Colors Everywhere */' not in content:
        content = re.sub(r'(</head>)', override_style + r'\\n  \1', content, flags=re.IGNORECASE)
        
    # Standardize header hero section if old bg-breadcrumb is there
    # Replace bg-dark in specific elements but not everywhere blindly, primarily headers
    old_header = re.search(r'<!-- Header Start -->.*?<div class="container-fluid bg-breadcrumb.*?<!-- Header End -->', content, re.DOTALL)
    if old_header:
        # Extract title if possible
        title_match = re.search(r'<h1.*?>(.*?)</h1>', old_header.group(0), re.DOTALL | re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else name_without_ext.replace('-', ' ').title()
        
        new_header = f'''<!-- Modern Hero Start -->
    <div class="new-hero" style="min-height: 450px; height: 50vh; display: flex; align-items: center; justify-content: center; text-align: center; background: linear-gradient(135deg, #FFF3E0 0%, #E8F5E9 100%);">
      <div class="container relative z-index-2">
        <h1 class="hero-title" style="font-size: 3rem; color: var(--text-main); font-weight: 700; text-transform: uppercase;">
          <span style="color: var(--primary);">{title}</span>
        </h1>
        <p class="hero-subtitle mx-auto mt-3" style="font-size: 1.25rem; color: #555; max-width: 700px;">
          Experience top-tier service tailored to your needs. Explore our comprehensive offerings and enjoy a seamless journey.
        </p>
      </div>
    </div>
    <!-- Modern Hero End -->'''
        content = content.replace(old_header.group(0), new_header)

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Updated {basename}")

print("Batch theme update completed!")
