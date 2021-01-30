
# XPath库的使用
[toc]
XPath，全称XML Path Language，即XML语言，最初是用来搜寻XML文档的，但同样也适用于HTML文档的搜索。
XPath的选择功能很强大，它提供了非常简洁的路径选择表达式。另外，它还提供了100个内建函数，用于字符串、数值、时间的匹配以及节点、序列的处理。更多文档可访问官方网站：https://www.w3.org/TR/xpath
<table align="center">
<caption> 表1 XPath常用规则<caption>
<tr>
 <th>表达式</th>
 <th> 描述</th>
 </tr>
 <tr>
 <th>nodename</th>
 <th>选取此节点的所有子节点</th>
 </tr>
 <tr>
    <th>/</th> <th>从当前节点选取直接子节点 </th>
 </tr>
 <tr>
    <th>//</th> <th>从当前节点选取子孙节点 </th>
 </tr>
 <tr>
    <th>.</th> <th>选取当前节点</th>
 </tr>
 <tr>
    <th>.. </th> <th>选取当前节点的父节点</th>
 </tr>
 <tr> 
    <th>@ </th> <th>选取属性</th>
 </tr>
</table>
例如：

//title[@lang='eng']

这就是一个XPath规则，它代表选择所有名称为title，同时属性为lang的值为eng的节点。
## lxml party
首先导入lxml库中的etree模块，etree模块可以自动修正HTML文本，即使文本是一个完整的HTML结构。
tostring()方法可以输出修正后的HTML代码，但返回结果是bytes类型。使用encode()方法将其转化为str类型。
## 选取节点
### 子节点
`one.py`中的`html.xpath()`方法中使用`//*`。`//`表示选取所有符合要求的节点，`*`表示匹配所有节点。
```python
from lxml import etree
html = etree.parse('./text.html', etree.HTMLParser())
result = html.xpath('//*') 
# result返回为一个list，每个元素是Element类型
'''
[<Element html at 0x1aca27d7f48>, <Element body at 0x1aca47700c8>, <Element div at 0x1aca4770188>, <Element ul at 0x1aca47701c8>, <Element 
li at 0x1aca4770208>, <Element a at 0x1aca4770488>, <Element li at 0x1aca4770388>, <Element a at 0x1aca47704c8>, <Element li at 0x1aca4770548>, <Element a at 0x1aca4770288>, <Element li at 0x1aca4770588>, <Element a at 0x1aca47705c8>, <Element li at 0x1aca4770608>, <Element a at 0x1aca4770648>]
'''
# 若*换为li，则选取所有li节点
result = html.xpath('//li')
result = html.xpath('//li/a')#所有li节点下的直接a子节点
result = html.xpath('//li//a')#所有li节点下的所有a子孙节点
```
### 父节点
可以用`..`来查找父节点，或者使用`parent::`来获取父节点，如：
```python
result = html.xpath('//a[@href="link4.html"]/../@class')
# 或者
result = html.xpath('//a[@href="link4.html"]/parent::/@class')
```
<p style="border-left-style:solid;border-left-color:teal;border-left-width:5px;background-color:#ddffff;padding:5px"><font style="color:red">
Note: `/namenode`应该表示当前的namenode的位置</font> </p>

### 属性匹配
在选取时可以通过`@符号进行属性过滤。比如，这里如果选取class为`item-0`的节点，可以这样
```python
result = html.xpath('//li[@class="item-0"]')
```
### 属性多值匹配
某些节点的属性值有多个，我们可以选取部分内容进行匹配，例如
```python
from lxml import etree
text = '''
<li class="li li-first" name="item"><a>first</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, li)]/a/text()')
print(result)
#输出为
['first']
```
此时使用`contains()`方法进行部分内容的匹配

同时也可进行多个属性匹配，即一个节点有多个属性，为准确匹配，可以利用多属性匹配，但是需要用`and`连接，如：
```python
result = html.xpath('//li[contains(@class, li) and @name="item"]')
print(result)
# 输出为
['first']
```
### 按序选择
在选择某些属性时可能匹配多个节点，但是我们只想要其中的某个节点，此时可以利用中括号`[]`传入索引的方法获取特定次序的节点，如
```python
result = html.xpath('//li[1]/a/text()')
result = html.xpath('//li[last()]/a/text()')
result = html.xpath('//li[position()<3]/a/text()')
result = html.xpath('//li[last()-2]/a/text()')
# 输出为
['first item']
['fifth item']
['first item', 'second item']
['third item']
```
`[]`中的函数或序号代表节点的位置，节点的位置按前后顺序从1到`last()`。更多函数可参考 http://www.w3school.com.cn/xpath/xpath_functions.asp

### 节点轴的选择
XPath中提供了很多节点轴选择方法，包括获取子元素、兄弟元素、父元素、祖先元素等，示例如下：
```python
result = html.xpath('//li[1]/ancestor::*')
result = html.xpath('//li[1]/ancestor::div')
result = html.xpath('//li[1]/attribute::*')
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
```
在这里我们使用了`ancestor`、`attribute`、`child`轴分别可获取祖先节点、属性值、子节点，还可以使用`descendant`轴获取所有子孙节点，使用`following`轴获取当前节点之后的所有节点，`following-sibling`轴获取当前节点之后的所有同级节点，更多节点轴的使用可参考 http://www.w3school.com.cn/xpath/xpath_axes.asp
