while True:
    r,n=map(int,input().split())
    if r==-1:
        break
    lst=list(map(int,input().split()))
    army=[]
    for i in lst:
        if i not in army:
            army.append(i)
    army.sort()
    n=len(army)
    num=0
    k=0
    while k<n:
        if army[k]+r>=army[-1]:
            num+=1
            break
        else:
            for i in range(k,n):
                if army[i]>army[k]+r:
                    s=i-1
                    break
            if army[s]+r>=army[-1]:
                num+=1
                break
            else:
                for j in range(s,n):
                    if army[j]>army[s]+r:
                        num+=1
                        k=j
                        break
    print(num)    