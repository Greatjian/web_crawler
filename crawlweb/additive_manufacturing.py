import requests
from bs4 import BeautifulSoup

def additive_manufacturing():
    result = []
    target_root = "http://additivemanufacturing.com/news/page/"
    url = "http://additivemanufacturing.com/news/page/"
    for i in range(3):
        article_list = []
        time_list = []
        link_list = []
        content_list = []
        r = requests.get(target_root+"{}".format(i+1))
        if r:
            soup = BeautifulSoup(r.text, 'html.parser')
            x = soup.find_all('header', "entry-header")
            for y in x:
                z=y.find('a')
                link_list.append(z['href'])#.encode('utf-8'))
                article_list.append((z.string))#.encode('utf-8'))
                time=y.find('time')
                time_list.append(time.string)
            for link in link_list:
                content = requests.get(link)
                content_soup = BeautifulSoup(content.text, 'html.parser')
                if content_soup.find('div', 'entry-content'):
                    x = content_soup.find('div', 'entry-content')
                try:
                    y = x.find_all('p')+x.find_all('ul')
                    article_content = ''
                    for z in y:
                        if z:
                            t = z.text
                            article_content = article_content + t.encode('ascii', 'ignore').decode("utf-8").replace('\n',' ')#.encode('utf-8')
                        else:
                            article_content = 'Not Accessible'
                except:
                    article_content = 'Not Accessible'
                content_list.append(article_content)
            for a, t, l, c in zip(article_list, time_list, link_list, content_list):
                result.append((url, a, t, l, c))
    # print(result)
    return result

# additive_manufacturing()