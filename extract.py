with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('class="new-hero"')
start = text.rfind('<', 0, start)
end = text.find('<!-- Bento Grid Features & Services -->')
print(text[start:end])
