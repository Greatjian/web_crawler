import requests
from bs4 import BeautifulSoup

def popsci_science():
    result = []
    target_root = "http://www.popsci.com/science"
    url = "http://www.popsci.com/science"
    article_list = []
    time_list = []
    link_list = []
    content_list = []
    r = requests.get(target_root)
    if r:
        soup = BeautifulSoup(r.text, 'html.parser')
        view_contents = soup.find_all('div', "view-content")
        for view_content in view_contents:
            y=view_content.find_all('h3')
            for z in y:
                content=z.find('a')
                link_list.append('http://www.popsci.com'+content['href'])#.encode('utf-8'))
                article_list.append(content.string)#.encode('ascii', 'ignore').encode('utf-8'))
            times=view_content.find_all('span','date')
            for time in times:
                time_list.append(time.text.replace('posted ','').replace('st','').replace('nd','').replace('rd','').replace('th',''))#.encode('utf-8'))
        for link in link_list:
            content = requests.get(link)
            content_soup = BeautifulSoup(content.text, 'html.parser')
            if content_soup.find('div', 'content'):
                x = content_soup.find('div', 'content')
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
    # print(article_list)
    return result

# popsci_science()