import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Nav: From <nav to </nav> ? Let's see if that covers it.
nav_m = re.search(r'<nav.*?</nav>', text, re.DOTALL)
print("Nav length:", len(nav_m.group(0)) if nav_m else 0)

# Footer: from <div class="ultra-footer"> or similar? Let's check <!-- Footer Start --> to end of the footer div.
# Instead of comments, let's just find the first <!-- Footer Start --> to <!-- Copyright End --> maybe?
footer_m = re.search(r'(<!-- Footer Start -->.*?<!-- Copyright End -->)', text, re.DOTALL)
print("Footer length:", len(footer_m.group(1)) if footer_m else 0)

# Marquee / scrolling ticker
marquee_m = re.search(r'<div class="scrolling-ticker".*?</div>\s*</div>', text, re.DOTALL)
print("Marquee length:", len(marquee_m.group(0)) if marquee_m else 0)

