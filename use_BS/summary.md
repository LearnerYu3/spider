# 使用Beautiful Soup
BS是一个强大的解析工具，借助网页的结构和属性等特性来解析网页。BS是python的一个HTML或XML的解析库，可以用它来方便的从网页中提取数据。
* BS提供一些简单的、python式的函数处理导航、搜索、修改分析树等功能。
* BS自动将输入文档转换为Unicode编码，输出文档转换为UTF-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时你仅仅需要说明一下原始编码方式就可以了。
* BS已成为和lxml、html6lib一样出色的python解释器，为用户灵活的提供不同的解析策略或强劲的速度。

BS在解析时实际上依赖解析器，他除了支持Python标准库中的HTML解析器外，还支持一些第三方解析器（比如 lxml）
<table style="align=center">
<caption>BS支持的解释器</caption>
<tr>
    <th>解析库</th> <th>使用方法</th> <th>优势</th> <th> 劣势</th>
</tr>
<tr>
<td>Python标准库</td> <td>BeautifulSoup(markup,"html.parser")</td> <td>Python的内置标准库、执行速度适中、文档容错能力强</td> <td>Python2.7.3及Python3.2.2之前的版本文档容错能力差</td>
</tr>
<tr>
    <td>lxml HTML解析器</td> <td>BeautifulSoup(markup, "lxml")</td> <td>速度快、文档容错能力强</td> <td>需要安装C语言库</td>
</tr>
<tr>
    <td>lxml XML解析器</td> <td>BeautifulSoup(markup,"xml")</td> <td>速度快、唯一支持XML文档的解析器</td> <td>需要安装C语言库</td>
</tr>
<tr>
    <td>html5lib</td> <td>BeautifulSoup(markup, "html5lib")</td> <td>最好的容错性、以浏览器的方式解析文档、生成HTML5格式的文档</td> <td>速度慢、不依赖外部扩展</td>
</tr>
</table>
从表中可以看出，lxml解析器有解析 HTML 和 XML 的功能。如果使用 lxml，那么在初始化 BS 时，可以把第二个参数改为 lxml 即可

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
```
<font style="color:red">Note : 这里的 html 是 markup 及 HTML 文本 (字符串)，不是未读取的`.html`文档 </font>

```python
soup = BeautifulSoup(html, 'lxml')# html为text.html文档内容的字符串
print(soup.title.string)
print(soup.p)
# 结果为
'''
The Dormouse's story
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
'''
```
这里可以看出这种节点的选择方式只会选择第一个匹配的节点，其它后面的节点都会被忽略。

* 获取节点名

```python
print(soup.title.name)
>>> title
```
* 获取属性

```python
print(soup.p.attrs)
print(soup.p.attrs['name'])
>>> {'class': ['title'], 'name': 'dormouse'}
>>> dormouse
# 或者可以省去 attrs
print(soup.p['name'])
>>> dormouse
```
这里需要注意，有的返回结果是字符串，有的返回结果是字符串组成的列表。比如，`name`属性的值是唯一的，返回的结果就是单个字符串。而对于`class`，一个节点元素可能有多个 class，所以返回的是列表。
* 嵌套选择

在上面的例子中，我们知道每一个返回的结果都是 bs4.element.Tag 类型，它同样可以进行下一步的选择，比如：
```python
print(soup.head.title)
print(type(soup.head.title))
>>> <title>The Dormouse's story</title>
>>> <class 'bs4.element.Tag'>
```
可以看出在调用`head`之后再次调用`title`选择的节点元素仍然是 `bs4.element.Tag` 类型
* 关联选择

 1. 子节点和子孙节点

    选取节点元素之后，如果想要获取它的直接子节点，可以调用 contents 属性，
    ```python
    print(soup.p.contents)
    >>> [<b>The Dormouse's story</b>]
    ```
    返回结果是列表形式，更直接的例子如`associated_option.py`中的结果
    ```python
    >>> ['\n    once upon a time there were three little sisters;\n    ', <a class="sister" href="http://example.com/exp" id="link1">
    <span>exp</span>
    </a>, '\n', <a class="sister" href="http://example.com/abc" id="link2">abc</a>, '\nand\n', <a class="sister" href="http://example.com/title" id="link3">title</a>, '\nand they are very happy.\n']
    ```
    p节点既包含文本，又包含节点，最后以列表的形式统一返回。

    调用`children`属性，返回的结果是迭代器类型。
    ```python
    print(soup.p.children)
    >>> <list_iterator object at 0x00000212E5EF0C48>
    # 使用 for 循环输出相应的内容
    for i, child in enumerate(soup.p.children)
    ```
    要想得到所有的子孙节点，可以调用`descendants`属性
    此时返回结果是生成器类型。

2. 父节点和祖父节点
   
   如果想要获取某个节点元素的父节点，可以调用 `parent` 属性，想要获取所有的祖先节点，可以调用所有的 `parents` 属性
3. 兄弟节点
   
   可以调用 `next_sibling` 和 `previous_sibling` 分别获取节点的下一个和上一个兄弟元素，`next_siblings` 和 `previous_siblings` 则分别返回后面和前面的兄弟节点。
4. 提取信息
   
   如果返回节点是单个节点，那么可以直接调用 `string`、`attrs` 等属性获得其文本和属性，如果返回结果是多个节点的生成器，则可以转为列表后取出某个元素，然后再调用 `string`、`attrs` 等属性获取相应的文本和属性。

## 方法选择器
前面所述的选择方法都是通过属性来选择的，这种方法非常快，但是如果进行比较复杂的选择的话，它就比较烦琐，不够灵活。我们可以使用其它的方法

* find_all()
  
  查询所有符合条件的元素。给它传入一些属性或文本，就可以得到符合条件的元素。
  
  它的 API ：`find_all(name, attrs, recursive, text, **kwargs)`
  1. name 
    
     可以根据节点名来查询元素，如 `methods.py` 中
     ```python
     soup = soup.find_all(name='ul')
     ```
     返回结果类型是列表类型，每个元素都是`bs4.element.Tag`类型
  2. attrs

     根据属性来查询，如
     ```python
     print(soup.find_all(attrs={'id': 'list-1'}))
     print(soup.find_all(attrs={'name': 'elements'}))
     ```
     这里查询的时候传入的是 `attrs` 参数，参数的类型是字典类型，得到的结果是列表形式。也可以直接传入参数
     ```python
     print(soup.find_all(id='list-1'))
     print(soup.find_all(class_='element))
     # 由于class是python中的关键字，所以这里使用class_
     ```
  3. text
      
      text 参数可用来匹配节点的文本内容，传入的形式可以是字符串，也可以是正则表达式对象，比如
      ```python
       print(soup..find_all(text=re.compile('link')))
      ```
* find
  
  此方法返回的结果是单个元素，即第一个匹配的元素，而`find_all`返回的结果是所有匹配的元素组成的列表。

* others
  
  还有许多查询方法和 `find_all()`、`find()` 方法完全相同，只不过查询范围不同
   
   1. find_parents( ) 和 find_parent( )
   2. find_next_siblings( ) 和 find_next_sibling( )
   3. find_previous_siblings( ) 和 find_previous_sibling( )
   
## CSS 选择器

BS还提供了CSS选择器，只需调用 `select()` 方法，传入相应的 CSS 选择器即可，如 `CSS_select.py` 中:
```python
print(soup.select('.panel.panel-heading'))
print(soup.select('ul li'))
print(soup.select('#link-2 .element'))
```
返回的结果均是符合 CSS 选择器的节点组成的列表，元素的类型依然是`bs4.element.Tag`。
* 嵌套选择
  ```python
  for ul in soup.select('ul'):
      print(ul.select('li'))
  ```

* 获取属性
  ```python
  for ul in soup.select('ul'):
      print(ul['id'])
      print(ul.attrs['id'])
  ```
  由于返回的节点类型是 `Tag` 类型，所以依然可以用字典的方法获取属性
  
* 获取文本
  可以使用之前使用的 `string` 属性，还可以使用 `get_text()`,