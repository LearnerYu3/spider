from lxml import etree

text = '''
<li class="li li-first" name="item"><a>first</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, li)]//a/text()')
print(result)
resutl1 = html.xpath('//li[contains(@class,li) and @name="item"]//a/text()')
print(resutl1)
