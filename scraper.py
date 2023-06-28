from bs4 import BeautifulSoup
import requests

def scrape_google(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    allData = soup.find_all("div",{"class":"g"})

    g=0
    datalist = [ ]
    l={}
    for i in range(0,len(allData)):
        link = allData[i].find('a').get('href')

        if(link is not None):
            if(link.find('https') != -1 and link.find('http') == 0 and link.find('aclk') == -1):
                g=g+1
                l["link"]=link
                try:
                    l["title"]=allData[i].find('h3').text
                except:
                    l["title"]=None

                try:
                    l["description"]=allData[i].find("span",{"class":"aCOpRe"}).text
                except:
                    l["description"]=None
                l["position"]=g
                datalist.append(l)
                l={}
            else:
                continue
        else:
            continue

    return datalist




# curl -X POST -H "Content-Type: application/json" -d '{"url":"https://www.google.fr/search?q=fermob;ie=utf-8&amp;oe=utf-8&amp;num=10"}' http://localhost:5000/scrape