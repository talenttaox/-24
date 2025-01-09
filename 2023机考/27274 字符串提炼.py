import math
s=str(input())
length=len(s)
m=int(math.log2(length))
lst=[]
for i in range(m+1):
    lst.append(s[2**i-1])
l,r=0,m
out=''
while l<r:
    out+=str(lst[l])+str(lst[r])
    l+=1
    r-=1
if l==r:
    out+=str(lst[l])
print(out)
