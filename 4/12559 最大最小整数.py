n=int(input())
lst=[]
lst=list(map(str,input().split()))
for i in range(n-1):
    for j in range(i+1,n):
        if lst[j]+lst[i]>lst[i]+lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
a=''
for i in lst:
    a+=i
for i in range(n-1):
    for j in range(i+1,n):
        if lst[j]+lst[i]<lst[i]+lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
b=''
for i in lst:
    b+=i
print(a,b)