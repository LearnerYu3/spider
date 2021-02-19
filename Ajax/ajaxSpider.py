import requests
import os
from hashlib import md5
from multiprocessing.pool import Pool

"""
from urllib.parse import urlencode
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None
"""


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if images:
                for image in images:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }


def save_image(item):
    try:
        if not os.path.exists('F:/codepy/spider/photos/' + item.get('title')):
            os.mkdir('F:/codepy/spider/photos/' + item.get('title'))
        try:
            response = requests.get(item.get('image'))
            if response.status_code == 200:
                file_path = 'F:/codepy/spider/photos/' + '{0}/{1}.{2}'.format(item.get('title'),
                                                                              md5(response.content).hexdigest(), 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                else:
                    print('Already Download', file_path)
        except requests.ConnectionError:
            print('Failed to Save Image')
    except:
        pass


def main(url):
    json = get_page(url)
    if get_images(json):
        for item in get_images(json):
            print(item)
            save_image(item)


if __name__ == '__main__':
    pool = Pool()
    groups = []
    f = open('./Ajax/url.txt', 'r', encoding='utf-8')
    for line in f.readlines():
        url = line.strip('\n')
        groups.append(url)
    f.close()
    pool.map(main, groups)
    pool.close()
    pool.join()

"""
GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x*20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
"""
