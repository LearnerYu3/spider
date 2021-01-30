from lxml import etree

html = etree.parse('use_XPath/text.html', etree.HTMLParser())
result = html.xpath('//li//a/text()')  # use text() get text content
print(result)
