import re

with open('c:/data/newc/about/service.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure we don't duplicate
if '/* Enforce New Theme Colors Everywhere */' not in text:
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
      /* Optional: Update the breadcrumb background to a modern gradient rather than default blue */
      .bg-breadcrumb {
        background: linear-gradient(135deg, rgba(255, 94, 0, 0.95), rgba(232, 93, 4, 0.85)), url(../img/breadcrumb.png) center center no-repeat;
        background-size: cover;
      }
    </style>
'''
    text = re.sub(r'(</head>)', override_style + r'\n  \1', text, flags=re.IGNORECASE)

with open('c:/data/newc/about/service.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected new theme colors to service.html.")
