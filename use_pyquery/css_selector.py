from pyquery import PyQuery as pq

html = '''
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
doc = pq(html)
print(doc('#container .list .item-0'))
items = doc('.list')
li = items.find('li')  # select correspanding nodes
li1 = items.children('.active')  # select children nodes
div = items.parent()
# no spacing between the twwo attributes
div1 = doc('.item-1.active').parents()
print(li)
print(li1)
print(div1)
# traverse
lis = doc('li').items()
for li in lis:
    print(li)
