from bs4 import BeautifulSoup;
import urllib.request,urllib.parse,urllib.response
import ssl
url=input('Enter - ')


html=urllib.request.urlopen(url).read();
soup=BeautifulSoup(html,'html.parser');
tags=soup('a');

for tag in tags:
    print(tag.get('href',None))



