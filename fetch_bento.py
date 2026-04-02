import re

with open('c:/data/newc/about/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'class="bento-section"(.*?)</section>', text, re.DOTALL | re.IGNORECASE)
if match:
    # Print the first few lines of it
    print(match.group(0)[:1500])
