n,m=map(int,input().split())
rank=list(map(int,input().split()))
rank.sort()
num=rank[-1]-rank[0]
if n>1:
    lst=[]
    for i in range(len(rank)-1):
        lst.append(rank[i+1]-rank[i])
    lst.sort(reverse=True)
    lst=lst[:m-1]
    for i in lst:
        num-=i
print(num)