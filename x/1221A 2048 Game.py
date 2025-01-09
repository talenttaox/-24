n=int(input())
for i in range(n):
    num=int(input())
    lst=list(map(int,input().split()))
    lst1=[]
    for i in lst:
        if i<=2048:
            lst1.append(i)
    if sum(lst1)>=2048:
        print('YES')
    else:
        print('NO')