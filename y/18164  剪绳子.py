import heapq
n=int(input())
length=[int(i) for i in input().split()]
tot=0
heapq.heapify(length)
while len(length)>1:
    a=heapq.heappop(length)
    b=heapq.heappop(length)
    tot+=a+b
    heapq.heappush(length,a+b)
print(tot)