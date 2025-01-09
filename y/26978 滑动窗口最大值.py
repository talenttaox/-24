import heapq
n,k=map(int,input().split())
nums=[-int(i) for i in input().split()]
heap=[]
out=[]
for i in range(k):
    heapq.heappush(heap,[nums[i],i])
out.append(-heap[0][0])
for i in range(k,n):
    heapq.heappush(heap,[nums[i],i])
    while heap[0][1]<=i-k:
        heapq.heappop(heap)
    out.append(-heap[0][0])
print(' '.join(map(str,out)))
