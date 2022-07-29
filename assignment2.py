#Week 3 programming assignment 2;




from bs4 import BeautifulSoup;
import urllib.request,urllib.parse,urllib.response
import ssl
import re;
count=0;

ctx=ssl.create_default_context()
ctx.check_hostname=False;
ctx.verify_mode=ssl.CERT_NONE;

link='http://py4e-data.dr-chuck.net/known_by_Kerry.html';


while True:
 if count>=7:
    break;         
 html_page=urllib.request.urlopen(link,context=ctx).read();
 soup2=BeautifulSoup(html_page,'html.parser');
 links=soup2('a');
 link=links[17].get("href");
 count+=1;


print(link)