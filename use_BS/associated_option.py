from bs4 import BeautifulSoup

html = """
<html><head><title>the dormouse's story</title></head>
<body>
<p class="story">
    once upon a time there were three little sisters;
    <a href="http://example.com/exp" class="sister" id="link1">
<span>exp</span>
</a>
<a href="http://example.com/abc" class="sister" id="link2">abc</a>
and
<a href="http://example.com/title" class="sister" id="link3">title</a>
and they are very happy.
</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)
