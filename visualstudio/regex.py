import re
inp=input("Enter File Name: ")
handle=open(inp)
sum=0
lst=list()
for line in handle:
    num=re.findall('[0-9]+',str(line))
    for i in num:
        lst.append(i)
for j in lst:
    sum=sum+int(j)
print(sum)
