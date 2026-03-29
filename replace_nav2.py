import codecs

def replace_nav():
    with codecs.open(r'c:\data\newc\about\index3.html', 'r', 'utf-8') as f:
        html = f.read()

    with codecs.open(r'c:\data\newc\about\new_nav.txt', 'r', 'utf-8') as f:
        nav = f.read()

    start_str = "<!-- Sticky Navbar & Hero Start -->"
    end_str = "  <!-- New Age Cinematic Hero -->"

    if start_str in html and end_str in html:
        start_idx = html.find(start_str)
        end_idx = html.find(end_str)
        if start_idx < end_idx:
            new_html = html[:start_idx] + start_str + "\n" + nav + "\n" + html[end_idx:]
            with codecs.open(r'c:\data\newc\about\index3.html', 'w', 'utf-8') as f:
                f.write(new_html)
            with open(r'c:\data\newc\about\python_success.txt', 'w') as f:
                f.write("Diddit")

if __name__ == '__main__':
    replace_nav()