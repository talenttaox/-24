n,k=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort(reverse=True)
tot=sum(lst)
res=k
while True:
    if res==1:
        print(f"{tot:.3f}")
        break
    ave=tot/res
    if lst[0]<=ave:
        print(f"{ave:.3f}")
        break
    else:
        res-=1
        tot-=lst[0]
        lst=lst[1:]
    