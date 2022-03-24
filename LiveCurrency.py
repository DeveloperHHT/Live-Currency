import requests
from bs4 import BeautifulSoup

url="https://www.doviz.com"

response = requests.get(url)

içerik=response.content

soup = BeautifulSoup(içerik,"html.parser")

birimler=[]

for i in soup.findAll("span",{"class":"name"}):

    birimler.append(i.text)

değerler=[]

for i in soup.findAll("span",{"class":"value"}):

    değerler.append(i.text)

for i,j in zip(birimler,değerler):

    print(i+" :",j)