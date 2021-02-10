# 使用 pyquery
## 初始化
需要传入 HTML 文本来初始化一个 PyQuery 对象，初始化方式有多种，直接传入字符串，传入 URL，传入文件名，等等。
* 字符串初始化
  ```python
  from pyquery import PyQuery as pq
  doc = pq(html)
  print(doc('li'))
  ```
  这里首先引入 PyQuery 对象，然后声明了一个 HTML 字符串，并将其当作参数传递给 PyQuery 类，这样就完成了初始化，然后传入 CSS 选择器

* URL 初始化
  还可以传入网页的 URL，如
  ```python
  doc = pq(url='https://www.baidu.com')
  print(doc('title'))
  ```
  PyQuery 对象会先请求这个 URL，然后用得到的 HTML 内容完成初始化，这其实就相当于用网页的源代码以字符串的形式传递给 PyQuery 类来初始化。等同于
  ```python
  import requests
  doc = pq(requests.get('https://www.baidu.com').text)
  print(doc('title'))
  ```

* 文件初始化
  还可以传递本地文件名
  ```python
  doc = pq(filename='demo.html')
  ```
## CSS 选择器
```python
doc = pq(html)
print(doc('#container .list li'))
```
其结果类型仍然是 PyQuery 类型。
## 查找节点
* 子节点
  
  查找子节点时，需要用到 find() 方法，此时传入的参数是 CSS 选择器
  ```python
  items = doc('.list')
  lis = items.find('li')
  ```
  `find()`方法会将符合条件的所有节点选择出来，即查找的范围是节点的所有子孙节点，结果都是 PyQuery 类型。如果只想查找子节点，可以用`children()`方法
  ```python
  lis = items.children('.active') #选出子节点中class为active的节点
  ```
* 父节点
  
  可以使用`parent()`方法来获取某个节点的父节点，使用`parents()`方法获取祖先节点，同样可以传入`CSS选择器`来选取某个特定的节点
* 兄弟节点
  
  可使用`siblings()`方法获取所有符合条件的兄弟节点
## 遍历
由于pyquery返回的结果不是列表，所以对于多个节点的情况，我们就需要遍历来获取了。此时需要调用`items()`方法
```python
doc = pq(html)
lis = doc('li').items() #返回generator类型
for li in lis:
    print(li)
```
## 获取信息
* 获取属性
  
  调用`attr()`方法来获取属性，在方法中传入属性的名称，就可得到属性值
  ```python
  a = doc('.item-0 .active a')
  print(a.attr('href')) # 或者
  print(a.attr.href)
  ```
* 获取文本

  获取节点后可以调用`text()`方法来获取文本，但是如果想要获取节点内部的 HTML 文本，就要调用`html()`方法。
  
  注意，`html()`方法返回的是第一个符合条件的节点的内部的 HTML 文本，而`text()`方法返回的是所有符合条件的节点内部的纯文本，中间用一个空格符隔开，返回结果是字符串。所以当匹配结果是多个节点时，此时想要获取每个节点内部的 HTML 文本，就需要遍历每个节点，而`text()`方法不需要遍历就可以获取，并且它将所有的节点取文本之后合并成一个字符串。
## 节点操作
pyquery 提供了一些方法来对节点进行动态修改
  
* addClass 和 removeClass
* attr、text 和 html
* remove
## 伪类选择器
CSS 选择器支持多种多样的伪类选择器，可参考 http://www.w3school.com.cn/css/index.asp
