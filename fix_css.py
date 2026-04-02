import re
import glob

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

root_style_m = re.search(r'<style>\s*:root\s*\{.*?</style>', index_content, re.DOTALL)
if not root_style_m:
    print("Could not find root style in index.html!")
    exit(1)

root_style = root_style_m.group(0)

# Also adding our absolute enforces
enforce_style = '''
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
    
    # Check if the full index root variables are in this file: we check for a specific distinct variable, e.g. '--bg-light:' or '--text-main:'
    if '--bg-light:' not in content:
        # It's missing the full variables! Let's inject root_style before </head>
        content = content.replace('</head>', f'{root_style}\n  </head>')

    # Ensure enforce style is present too
    if '/* Enforce New Theme Colors Everywhere */' not in content:
        content = content.replace('</head>', f'{enforce_style}\n  </head>')

    if content != orig:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Injected CSS variables into", file)

print("CSS variables sync complete.")
