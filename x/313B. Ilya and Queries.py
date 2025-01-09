str=input()
num=int(input())
lst=[0]
s=0
for i in range(len(str)-1):
    if str[i]==str[i+1]:
        s+=1
    lst.append(s)

for i in range(num):
    a,b=map(int,input().split())
    k=lst[b-1]-lst[a-1]
    print(k)