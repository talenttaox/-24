t=int(input())
output=[]
for i in range(t):
    n,x=map(int,input().split())
    number=list(map(int,input().split()))
    mod=[]
    for j in number:
        mod.append(j%x)
    total_mod=sum(mod)
    if total_mod%x==0:
        if mod.count(0)==n:
            output.append(-1)
        else:
            for k in range(0,n,1):
                if mod[k]!=0:
                    num=n-1-k
                    break
            for k in range(n-1,-1,-1):
                if mod[k]!=0:
                    num=max(num,k)
                    break
            output.append(num)
    else:
        output.append(n)
for i in output:
    print(i)