import re;


sum=0
file=open('reg-ex.txt');
for line in file:
    y=re.findall('[0-9]+',line)
    for item in y:
        converted_int=int(item)
        sum+=converted_int
print (sum)   

 

match2=re.search('t.*s$','Today the temperature is 27 celcius')
print(match2)



