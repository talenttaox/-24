n=int(input())
a=list(map(int,input().split()))
lst=[]
for i in range(n):
    lst.append([i+1-a[i],i+1+a[i]])
start=1
num=0
while True:
    if start>=n:
        break
    s=start
    for i in range(n):
        if lst[i][0]>start or lst[i][1]<=start:
            continue
        else:
            s=max(s,lst[i][1])
    num+=1
    start=s
    #print(start)
print(num)