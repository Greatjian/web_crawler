import requests
from bs4 import BeautifulSoup

def nature_scrape():
    result = []
    target_root = "https://www.nature.com/search?article_type=news&date_range=last_30_days&journal=news&order=relevance&page="
    url = "https://www.nature.com/search?article_type=news&date_range=last_30_days&journal=news&order=relevance"
    for i in range(5):
        article_list = []
        time_list = []
        link_list = []
        content_list = []
        r = requests.get(target_root+"{}".format(i+1))
        if r:
            soup = BeautifulSoup(r.text,'html.parser')
            for x in soup.find_all('a',{'data-track-click':'search_result_click'}):
                link_list.append(x['href'])#.encode('utf-8'))
                article_list.append(x.text)#.encode('utf-8'))
            for y in soup.find_all('time',{'itemprop':'datePublished'}):
                time_list.append(y.text)#.encode('utf-8'))
            for z in link_list:
                content = requests.get(z)
                content_soup = BeautifulSoup(content.text,'html.parser')
                x = content_soup.find_all('section',{'id':'article-body'})
                for y in x:
                    if y.find_all('div',{'class':'content no-heading cleared main-content'}):
                        for z in y.find_all('div',{'class':'content no-heading cleared main-content'}):
                            article_content = z.text
                            article_content = article_content.encode('ascii', 'ignore').decode("utf-8").replace('\n',' ')#.encode('utf-8')
                            content_list.append(article_content)
                    else:
                        content_list.append('Not Accessible')
            for a,t,l,c in zip(article_list,time_list,link_list,content_list):
                result.append((url,a,t,l,c))
    # print(result)
    return result
# nature_scrape()