n=int(input())
lst=list(map(int,input().split()))
lst.sort()
time=lst[0]
num=1
for i in range(1,n):
    if lst[i]>=time:
        time+=lst[i]
        num+=1
print(num)