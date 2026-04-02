import sys
import re

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Add CSS for global mobile fixes (typography and image sizes)
    mobile_css = '''
<style>
/* Global Mobile Responsiveness Fixes */
@media (max-width: 768px) {
    .display-4 { font-size: 2.5rem !important; }
    .display-5 { font-size: 2rem !important; }
    .display-6 { font-size: 1.75rem !important; }
    .fs-5 { font-size: 1rem !important; }
    .whatsapp-btn { width: 100%; text-align: center; }
    .row.g-4 { gap: 1rem !important; }
    section { padding: 3rem 0 !important; }
    .p-40-mobile { padding: 25px !important; }
}
@media (min-width: 769px) {
    .p-40-mobile { padding: 40px; }
}
</style>
'''
    if '/* Global Mobile Responsiveness Fixes */' not in text:
        head_end = text.find('</head>')
        if head_end != -1:
            text = text[:head_end] + mobile_css + text[head_end:]
            print(f"Added mobile CSS to {filename}")

    # 2. Fix massive padding hardcodes
    text = text.replace('padding: 40px;', 'padding: 40px;" class="p-40-mobile')
    text = text.replace('style="padding: 40px;" class="p-40-mobile', 'class="p-40-mobile"')

    # 3. Fix button overlaps on cards (Make them stack on mobile)
    text = text.replace('d-flex justify-content-between align-items-center mt-auto', 'd-flex flex-wrap justify-content-between align-items-center mt-auto gap-3')
    
    # 4. Fix Hero CTA Buttons (they might be sticking out)
    text = text.replace('<div class="d-flex align-items-center gap-2">', '<div class="d-flex flex-wrap align-items-center gap-3">')

    # 5. Fix "Mountain & Family Safety Feature" column ordering/stacking (Bootstrap usually handles this, but let's ensure image/text gap)
    text = text.replace('class="row align-items-center g-5"', 'class="row align-items-center g-4 g-lg-5"')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

fix_file('index.html')
fix_file('taxi-services.html')

