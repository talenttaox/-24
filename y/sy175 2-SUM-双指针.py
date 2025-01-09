n,k=map(int,input().split())
lst=list(map(int,input().split()))
i=0
j=n-1
num=0
while i<j:
    if lst[i]+lst[j]<k:
        i+=1
    elif lst[i]+lst[j]>k:
        j-=1
    elif lst[i]+lst[j]==k:
        num+=1
        i+=1
        j-=1
print(num)