def mintime(intervals):
    intervals.sort(key=lambda x:x[1])
    count=0
    i=0
    n=len(intervals)
    while i<n:
        testtime=intervals[i][1]
        count+=1
        while i<n and intervals[i][0]<=testtime:
            i+=1
    return count

k=int(input())
for i in range(k):
    n=int(input())
    intervals=[]
    for j in range(n):
        intervals.append(list(map(int,input().split())))
    print(mintime(intervals))