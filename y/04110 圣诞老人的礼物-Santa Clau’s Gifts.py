n,max=map(int,input().split())
lst=[]
for i in range(n):
    v,w=map(int,input().split())
    lst+=[v/w]*w
lst.sort(reverse=True)
print(f"{sum(lst[:max]):.1f}")