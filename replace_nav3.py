import codecs
import re

def replace_nav():
    with codecs.open(r'c:\data\newc\about\index3.html', 'r', 'utf-8') as f:
        html = f.read()

    with codecs.open(r'c:\data\newc\about\new_nav_full.txt', 'r', 'utf-8') as f:
        nav = f.read()

    # Search for the newly injected nav to replace it
    pattern = re.compile(r'<!-- Ultra Modern Floating Navbar Start -->.*?<!-- Ultra Modern Floating Navbar End -->', re.DOTALL)
    
    if pattern.search(html):
        new_html = pattern.sub(nav, html)
        with codecs.open(r'c:\data\newc\about\index3.html', 'w', 'utf-8') as f:
            f.write(new_html)
        print("Success! Executed replacement.")
    else:
        print("Failed to find pattern. Falling back to initial method...")
        pattern2 = re.compile(r'<!-- Sticky Navbar & Hero Start -->.*?<!-- New Age Cinematic Hero -->', re.DOTALL)
        if pattern2.search(html):
            new_html2 = pattern2.sub("<!-- Sticky Navbar & Hero Start -->\n" + nav + "\n  <!-- New Age Cinematic Hero -->", html)
            with codecs.open(r'c:\data\newc\about\index3.html', 'w', 'utf-8') as f:
                f.write(new_html2)
            print("Successfully fallback replaced!")

if __name__ == '__main__':
    replace_nav()
