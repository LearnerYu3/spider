from lxml import etree
text = """
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
"""
html = etree.HTML(text) #etree module can modify correct HTML text automatically.
'''
html = etree.parse('./text.html', etree.HTMLParser()) # can read HTML file directly to analyse.
'''
result = etree.tostring(html) # tostring method return the result which is bytes type.
result =result.decode('utf-8') # str type
search = html.xpath('//*') # * denote all nodes and the result of search is a list
print(search)