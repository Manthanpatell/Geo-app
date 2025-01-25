import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count=list()
link=input("Enter -")
url=urllib.request.urlopen(link).read()
# http://py4e-data.dr-chuck.net/comments_42.json
data=[json.loads(url)]
dic=data[0]
dic1=dic["comments"]
print(len(dic1))
for i in range(len(dic1)):
    for item in data:
        count.append(item["comments"][i]["count"])
sum=0
for i in count:
    sum=sum+int(i)
print(sum)