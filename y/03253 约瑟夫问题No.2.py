while True:
    n,p,m=map(int,input().split())
    if n==0 and m==0 and p==0:
        break
    lst=[i for i in range(1,n+1)]
    lst=lst[p-1:]+lst[:p-1]
    lst1=[]
    while len(lst)>1:
        if len(lst)>=m:
            lst1.append(lst[m-1])
            lst=lst[m:]+lst[:m-1]
        elif len(lst)<m:
            r=m%len(lst)
            if r!=0:
                lst1.append(lst[r-1])
                lst=lst[r:]+lst[:r-1]
            else:
                lst1.append(lst[-1])
                lst=lst[:-1]
    lst1.append(lst[0])
    print(",".join(map(str,lst1)))