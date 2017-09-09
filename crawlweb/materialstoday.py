import requests
from bs4 import BeautifulSoup

def materialstoday():
    result = []
    target_root = "http://www.materialstoday.com/news/2017-07/"
    url = "http://www.materialstoday.com/news/"
    article_list = []
    time_list = []
    link_list = []
    content_list = []
    r = requests.get(target_root)
    if r:
        soup = BeautifulSoup(r.text, 'html.parser')
        x = soup.find('div', "listContent")
        view_contents=x.find_all('div','articleSnippet')
        for view_content in view_contents:
            content=view_content.find('a')
            link_list.append(content['href'])#.encode('utf-8'))
            name=view_content.find('span')
            article_list.append(name.string)#.encode('ascii', 'ignore'))#.encode('utf-8'))
            time=view_content.find('span','articleDate')
            time_list.append(time.text)#.encode('utf-8'))
        for link in link_list:
            content = requests.get(link)
            content_soup = BeautifulSoup(content.text, 'html.parser')
            if content_soup.find('div', 'articleBody'):
                x = content_soup.find('div', 'articleBody')
            try:
                y = x.find_all('p')+x.find_all('ul')
                article_content = ''
                for z in y:
                    if z:
                        t = z.text
                        article_content = article_content + t#.encode('ascii', 'ignore').decode("utf-8").replace('\n',' ')#.encode('utf-8')
                    else:
                        article_content = 'Not Accessible'
            except:
                article_content = 'Not Accessible'
            content_list.append(article_content)
        for a, t, l, c in zip(article_list, time_list, link_list, content_list):
            result.append((url, a, t, l, c))
    # print(result)
    return result

# materialstoday()