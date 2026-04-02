import re

with open('c:/data/newc/about/service_retheme.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make double sure no extra </div> is there
text = text.replace(
'''<div class="bento-icon me-4" style="margin-bottom: 0;"><i class="fas fa-taxi"></i></div>
                </div>''',
'''<div class="bento-icon me-4" style="margin-bottom: 0;"><i class="fas fa-taxi"></i></div>'''
)

with open('c:/data/newc/about/service_retheme.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Also copy over completely replacing original service.html
import shutil
shutil.copyfile('c:/data/newc/about/service_retheme.html', 'c:/data/newc/about/service.html')

print("Copied rethemed service.html to main file.")
