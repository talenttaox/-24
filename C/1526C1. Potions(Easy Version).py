import heapq
n=int(input())
lst=list(map(int,input().split()))
a=[]
hp=0
num=0
for i in lst:
    if hp+i>=0:
        hp+=i
        num+=1
        if i<0:
            heapq.heappush(a,i)
    elif a and i>a[0]:
        hp+=i-heapq.heappop(a)
        heapq.heappush(a,i)
print(num)