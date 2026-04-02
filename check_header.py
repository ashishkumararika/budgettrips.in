import re

with open('c:/data/newc/about/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

with open('c:/data/newc/about/service.html', 'r', encoding='utf-8') as f:
    service_content = f.read()

# Let's see what the page header looks like in service.html and index.html
page_header_s = re.search(r'class="[^"]*page-header[^"]*".*?>', service_content)
print("Service page header:", page_header_s.group(0) if page_header_s else None)
