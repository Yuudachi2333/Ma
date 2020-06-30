import requests
from bs4 import BeautifulSoup

# url = 'https://www.runoob.com/python3/python3-tutorial.html'
# url_list=[]
# response = requests.get(url)
# r = response.text
# # print(r)
# data = BeautifulSoup(r)
# # print(data)
# url1 = data.find_all('div',class_='next-design-link')[0]
# a = url1.find('a')
# next_url = a.attrs.get('href')
# url_list.append(next_url)
# print(url_list)


def start(url):
    html = get_html(url)
    next_url = html_parse(html)
    if next_url != 0:
        print(next_url)
        start(next_url)


def get_html(url):
    response = requests.get(url)
    html = response.text
    # print(html)
    return  html

def html_parse(html):
    data = BeautifulSoup(html)
    try:
        url1 = data.find_all('div',class_='next-design-link')[0]
        a = url1.find('a')
        next_url = a.attrs.get('href')
        return next_url
    except AttributeError:
        print("end")
        return 0



if __name__ == '__main__':
    url = 'https://www.runoob.com/python3/python3-tutorial.html'
    # url = 'https://www.runoob.com/python3/python-topological-sorting.html'
    start(url)
