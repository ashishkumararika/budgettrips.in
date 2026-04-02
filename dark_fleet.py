import sys

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace variables in the Fleet Elite CSS
text = text.replace('background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);', 'background: #050505;')
text = text.replace('background: #ffffff;\n    border-radius: 24px;', 'background: #0a0a0a;\n    border-radius: 24px;')
text = text.replace('box-shadow: 0 10px 40px rgba(0,0,0,0.04);', 'box-shadow: 0 10px 40px rgba(0,0,0,0.4);')
text = text.replace('border: 1px solid rgba(0,0,0,0.03);', 'border: 1px solid rgba(212,175,55,0.1);')
text = text.replace('box-shadow: 0 20px 50px rgba(13, 110, 253, 0.12);', 'box-shadow: 0 20px 50px rgba(212, 175, 55, 0.15);')
text = text.replace('border-color: rgba(13, 110, 253, 0.1);', 'border-color: rgba(212, 175, 55, 0.3);')
text = text.replace('background: radial-gradient(circle at center, #f1f5f9 0%, #e2e8f0 100%);', 'background: radial-gradient(circle at center, #111 0%, #050505 100%);')

# Replace text colors in fleet
text = text.replace('color: #1e293b;', 'color: #fff;')  # text-dark equivalent
text = text.replace('color: #64748b;', 'color: #a0a0a0;') # text-muted
text = text.replace('color: #0d6efd;', 'color: #d4af37;') # primary blue to gold
text = text.replace('background: #ebf5ff;', 'background: rgba(212, 175, 55, 0.1);') # primary light badge bg

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Fleet section styled to dark luxury.")
