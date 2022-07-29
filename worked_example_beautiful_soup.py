from bs4 import BeautifulSoup;
import urllib.request,urllib.parse,urllib.response
import ssl
import re;
link  = "http://py4e-data.dr-chuck.net/comments_1603340.html"


#Ignoring ssl errors

ctx=ssl.create_default_context()
ctx.check_hostname=False;
ctx.verify_mode=ssl.CERT_NONE;
#assingment1

html=urllib.request.urlopen(link,context=ctx).read();
soup=BeautifulSoup(html,'html.parser');
#crummprint(soup)
tags=soup('span');
#print(tags)
sum=0;

for tag in tags:
    sum=sum+int(tag.get_text())
   
#print(sum) 




#Assignment2


link2='http://py4e-data.dr-chuck.net/known_by_Kerry.html';

html_page=urllib.request.urlopen(link2,context=ctx).read();
soup2=BeautifulSoup(html_page,'html.parser');

links=soup2('a');

for link in links:
    print(type(link.get('href')))









    