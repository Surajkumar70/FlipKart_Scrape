from bs4 import BeautifulSoup
import requests,json
from pprint import pprint
import json

from requests.models import HTTPBasicAuth
d=""
data=[]
for ii in range(1,11):
    url="https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"+str(d)
    response=requests.get(url) 
    htmlcontent=response.content
    soup=BeautifulSoup(htmlcontent,'html.parser')
    titles=[]
    prices=[]
    images=[]
    details=[]
    d=str(ii)
    for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):
        title=d.find('div',attrs={'class':'_4rR01T'})
        price=d.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
        image=d.find('img',attrs={'class':'_396cs4 _3exPp9'})
        detail=d.find_all('div',class_="col col-7-12")
        for i in detail:
            jk=i.find("ul").text
        titles.append(title.string)
        prices.append(price.string)
        images.append(image.get('src'))
        details.append(jk)
        data1={}
        for i,j,k,h in zip(title,price,images,details):
            data1["Name"]=i
            data1["price"]=j
            data1["Image"]=k
            data1["detail"]=h
            print(data1)
            data.append(data1)
s=open('Flipkart_Camera.json',"w")
d=json.dump(data,s,indent=4)
s.close()


