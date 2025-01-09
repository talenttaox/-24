def search(s,e,m,rock):
    left,right=s,e
    ans=0
    while left<right:
        mid=(left+right)//2
        s0=0
        num=0
        for i in range(1,n+2):
            if rock[i]-s0<mid:
                num+=1
            else:
                s0=rock[i]
        if num>m:
            right=mid
        else:
            left=mid+1
            ans=mid
    return ans

l,n,m=map(int,input().split())
rock=[0]
for i in range(n):
    rock.append(int(input()))
rock.append(l)
print(search(0,l+1,m,rock))