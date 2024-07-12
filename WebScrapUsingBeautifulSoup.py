import requests 
from bs4 import BeautifulSoup 
from lxml import etree 




def getDetails(productName):
    myURL = f'https://pharmeasy.in/search/all?name={productName}'
    r = requests.get(myURL) 
    soup = BeautifulSoup(r.content, 'html.parser')     
    dom = etree.HTML(str(soup))
    title = dom.xpath('//*[@id="__next"]/main/div/div/div/div[1]/div[1]/div/div/a/div[2]/div/div[1]/div/h1')[0].text


    return title

t = getDetails('metacin')
print(t)