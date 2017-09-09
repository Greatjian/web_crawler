import requests
from bs4 import BeautifulSoup

def threeders():
    result = []
    target_root = "http://www.3ders.org/internal-news/3d-printing-news-in-jul-2017.html"
    url = "http://www.3ders.org/internal-news/"
    article_list = []
    time_list1 = []
    time_list2 =[]
    link_list = []
    content_list = []
    r = requests.get(target_root)
    if r:
        soup = BeautifulSoup(r.text, 'html.parser')
        x = soup.find('div', "art-postcontent")
        view_contents=x.find_all('div','art-content-layout')
        for view_content in view_contents:
            contents=view_content.find_all('a')
            a=contents[0]['href']
            link_list.append('http://www.3ders.org/'+contents[0]['href'][a.index('/')+1:])#.encode('utf-8'))
            if len(contents)>3:
                link_list.append('http://www.3ders.org/' + contents[3]['href'][a.index('/')+1:])#.encode('utf-8'))
            name=view_content.find_all('p')
            article_list.append(name[0].text.replace('\n','').replace('\r','')[8:-7])#.encode('utf-8'))
            time_list1.append(name[1].text.replace('\n','').replace('\r','')[5:17])#.encode('utf-8'))
            if len(name)>2:
                article_list.append(name[2].text.replace('\n','').replace('\r','')[8:-7])#.encode('utf-8'))
                time_list1.append(name[3].text.replace('\n','').replace('\r','')[5:17])#.encode('utf-8'))
        del article_list[-1], time_list1[-1], link_list[-1]
        for time in time_list1:
            time_list2.append('2017.'+time[:time.index(',')].replace('Jul','7'))#.encode('utf-8'))
        for link in link_list:
            content = requests.get(link)
            content_soup = BeautifulSoup(content.text, 'html.parser')
            x = content_soup.find('div', 'art-layout-cell')
            try:
                y = x.find_all('p')+x.find_all('ul')
                article_content = ''
                for z in y:
                    if z:
                        t = z.text
                        k=t.encode('ascii', 'ignore').decode("utf-8").replace('\n', ' ')#.encode('utf-8')
                        if k[:9]=="Posted in" and z.find_all('a'):
                            break
                        article_content = article_content + t.encode('ascii', 'ignore').decode("utf-8").replace('\n',' ')#.encode('utf-8')
                    else:
                        article_content = 'Not Accessible'
            except:
                article_content = 'Not Accessible'
            content_list.append(article_content)
        for a, t, l, c in zip(article_list, time_list2, link_list, content_list):
            result.append((url, a, t, l, c))
    # print(result)
    return result

# threeders()

