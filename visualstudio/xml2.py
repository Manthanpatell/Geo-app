import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count=list()
sum=0
link=input("Enter-")
url=urllib.request.urlopen(link).read()

tags=ET.fromstring(url)
lst=tags.findall('comments/comment')
print('count',len(lst))

for item in lst:
        count.append(item.find('count').text)
for num in count:
    sum=sum+int(num)
print(sum)