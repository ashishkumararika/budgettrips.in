import codecs
import re

with codecs.open(r'c:\data\newc\about\index3.html', 'r', 'utf-8') as f:
    html = f.read()

with codecs.open(r'c:\data\newc\about\new_nav_full.txt', 'r', 'utf-8') as f:
    nav = f.read()

# Pattern: From <!-- Sticky Navbar & Hero Start --> to <!-- New Age Cinematic Hero -->
# But wait, my snippet in index3.html might not have <!-- Ultra Modern Floating Navbar Start -->. 
# Let's just find the start: <!-- Sticky Navbar & Hero Start -->
# and the end: <!-- New Age Cinematic Hero -->

pattern = re.compile(r'<!-- Sticky Navbar & Hero Start -->.*?<!-- New Age Cinematic Hero -->', re.DOTALL)

if pattern.search(html):
    print("Found the target to replace!")
    new_html = pattern.sub(nav + '\n\n  <!-- New Age Cinematic Hero -->', html)
    with codecs.open(r'c:\data\newc\about\index3.html', 'w', 'utf-8') as f:
        f.write(new_html)
    print("Successfully replaced nav!")
else:
    print("Failed to find pattern. Let me look for Navbar and New Age Cinematic Hero instead.")
    pattern2 = re.compile(r'<div class="container-fluid nav-bar p-0  mobile-safe-area-bottom".*?<!-- New Age Cinematic Hero -->', re.DOTALL)
    if pattern2.search(html):
        new_html = pattern2.sub(nav + '\n\n  <!-- New Age Cinematic Hero -->', html)
        with codecs.open(r'c:\data\newc\about\index3.html', 'w', 'utf-8') as f:
            f.write(new_html)
        print("Successfully replaced nav via pattern2!")
    else:
        print("Could not find any nav section!")
