import requests
from bs4 import BeautifulSoup

def spectrum_ieee_computing_scrape():
    result = []
    target_root = "http://spectrum.ieee.org/computing"
    url = "http://spectrum.ieee.org/computing"
    article_list = []
    time_list = []
    link_list = []
    content_list = []
    r = requests.get(target_root)
    if r:
        soup = BeautifulSoup(r.text,'html.parser')
        x=soup.find('div',"topic-articles")
        links=x.find_all('a')
        for link in links:
            link_list.append('http://spectrum.ieee.org/' + link['href'])#.encode('utf-8'))
            titles=link.find('h3')
            article_list.append(titles.string)#.encode('utf-8'))
            time=link.find('p')
            try:
                t=time.time.string
                t= t.encode('ascii', 'ignore').decode('ascii')#.encode('utf-8'))
                if len(t)<6:
                    t+='2017'
                time_list.append(t)
            except:
                time_list.append('01Jan2010')
        for z in link_list:
            content = requests.get(z)
            content_soup = BeautifulSoup(content.text,'html.parser')
            if content_soup.find('div', 'entry-content'):
                x = content_soup.find('div', 'entry-content')
            elif content_soup.find('div', 'transcript'):
                x = content_soup.find('div', 'transcript')
            else:
                x='None'
            try:
                y=x.find_all('p')+x.find_all('ul')
                article_content=''
                for z in y:
                    if z:
                        t = z.text
                        article_content = article_content+t.encode('ascii', 'ignore').decode("utf-8").replace('\n',' ')#.encode('utf-8')
                    else:
                        article_content='Not Accessible'
            except:
                article_content = 'Not Accessible'
            content_list.append(article_content)
        for a,t,l,c in zip(article_list,time_list,link_list,content_list):
            result.append((url,a,t,l,c))
    # print(result)
    return result
# spectrum_ieee_computing_scrape()
