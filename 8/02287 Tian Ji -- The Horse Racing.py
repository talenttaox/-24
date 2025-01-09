output=[]
while True:
    n=int(input())
    if n==0:
        break
    tian=list(map(int,input().split()))
    king=list(map(int,input().split()))
    tian.sort(reverse=True)
    king.sort(reverse=True)
    l_tian=l_king=0
    r_tian=r_king=n-1
    num=0
    while True:
        if tian[r_tian]>king[r_king]:
            r_tian-=1
            r_king-=1
            num+=1
        elif tian[l_tian]>king[l_king]:
            l_tian+=1
            l_king+=1
            num+=1
        else:
            if tian[r_tian]<king[l_king]:
                num-=1
            r_tian-=1
            l_king+=1
        if r_king<l_king:
            break
    output.append(num*200)
print('\n'.join(map(str,output)))