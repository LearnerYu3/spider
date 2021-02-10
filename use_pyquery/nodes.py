from pyquery import PyQuery as pq
html = '''
<div class="wrap">
Hello, World
<p>This is a paragraph</p>
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)
li.attr('name', 'link')
print(li)
li.text('change html')
print(li)
li.html('<span>change html</span>')
print(li)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())
