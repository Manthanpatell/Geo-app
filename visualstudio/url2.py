import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url=input('Enter - ')
count=int(input('Enter Count :'))
pos=int(input('Enter Position :'))-1
html=urllib.request.urlopen(url).read()

soup=BeautifulSoup(html,'html.parser')
href=soup('a')
#print(href)
for i in range(count):
    link=href[pos].get('href',None)
    print(href[pos].contents[0])
    html=urllib.request.urlopen(link).read()
    soup=BeautifulSoup(html,'html.parser')
    href=soup('a')