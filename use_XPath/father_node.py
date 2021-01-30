from lxml import etree

html = etree.parse('use_XPath/text.html', etree.HTMLParser())
# / donate current node
result = html.xpath('//a[@href="link4.html"]/../@class')
'''
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
'''
print(result)
'''
# match attribute
result = html.xpath('//li[@class="item-0"]')
'''
