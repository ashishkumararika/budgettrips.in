import re
import glob

def fix_quote_section(content):
    # Fix the dark background
    content = re.sub(
        r'background:\s*linear-gradient\([^)]*#050505[^)]*\);', 
        r'background: linear-gradient(135deg, #FFF9F2 0%, #FFF0DD 100%);', 
        content
    )
    # Fix border
    content = re.sub(
        r'border-top:\s*1px\s*solid\s*rgba\(212,\s*175,\s*55,\s*0\.1\);',
        r'border-top: 1px solid rgba(0, 0, 0, 0.05);',
        content
    )
    # Fix text color in quote-section
    content = re.sub(
        r'\.quote-section\s*\{([^\}]+)color:\s*#fff;',
        r'.quote-section {\1color: var(--text-main);',
        content
    )
    # Fix quote-icon color and opacity
    content = re.sub(
        r'\.quote-icon\s*\{([^\}]+)color:\s*#d4af37;',
        r'.quote-icon {\1color: var(--primary);',
        content
    )
    # Fix wanderlust-quote gradient
    content = re.sub(
        r'background:\s*linear-gradient\([^)]*#d4af37[^)]*\);',
        r'background: linear-gradient(45deg, var(--primary), #FF8C00, #E85D04);',
        content
    )
    # Fix quote-author color (it might not be explicitly set, let's inject it)
    if 'color: #a0a0a0;' in content:
        content = content.replace('color: #a0a0a0;', 'color: var(--text-muted);')
    return content

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '.quote-section' in content or '#050505' in content:
        new_content = fix_quote_section(content)
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Fixed quote section in", file)

