
"""
import urllib.request
import urllib.error
import socket
try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
except urllib.error.URLError as e:
    # isinstance(a, type) a表示实例对象, type是表示a是否匹配的对象
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
"""

"""
from urllib import parse, request

url = 'http://httpbin.org/post'
header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=header, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
"""

"""
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743' # https比http安全，不应使用
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
"""

"""
import http.cookiejar, urllib.request
filename = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
"""

"""
import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
} # 模拟浏览器访问，避免被认为是爬虫
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('ExploreSpecialCard-contentTag.*?question.*?>(.*?)</a>', re.S)
# 正则表达式选取正确的内容
titles = re.findall(pattern, r.text)
print(titles)
"""