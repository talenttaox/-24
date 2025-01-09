n,a,b=map(int,input().split())
water=list(map(int,input().split()))
left,right=0,n-1
num=0
sa,sb=a,b
while left<=right:
    if left==right:
        if sa>=sb:
            if sa>=water[left]:
                sa-=water[left]
            else:
                sa=a-water[left]
                num+=1
        else:
            if sb>=water[right]:
                sb-=water[right]
            else:
                sb=b-water[right]
                num+=1
        break
    if sa>=water[left]:
        sa-=water[left]
    else:
        sa=a-water[left]
        num+=1
    if sb>=water[right]:
        sb-=water[right]
    else:
        sb=b-water[right]
        num+=1
    left+=1
    right-=1
print(num)