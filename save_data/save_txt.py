import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
html = requests.get(url, headers=header).text
doc = pq(html)
items = doc('.ExploreCollectionCard-contentItem').items()
for item in items:
    question = item.find('a').text()
    answer = pq(item.find('.ExploreCollectionCard-contentExcerpt').html()).text()
    file = open('F://codepy//spider//save_data//explore.txt',
                'a', encoding='utf-8')
    file.write('\n'.join([question, answer]))
    file.write('\n' + '='*50 + '\n')
    file.close()
