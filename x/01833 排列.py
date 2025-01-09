m=int(input())
out=[]
for i in range(m):
    n,k=map(int,input().split())
    first_array=[int(i) for i in range(1,n+1)]
    last_array=[int(n-i) for i in range(n)]
    array=list(map(int,input().split()))
    for _ in range(k):
        if array==last_array:
            array=first_array
        else:
            for i in range(1,n):
                if array[-i]>array[-1-i]:
                    s=array[n-i-1]
                    lst2=array[n-i-1:]
                    lst2.sort()
                    for l in lst2:
                        if l>s:
                            c=l
                            break
                    lst1=array[:n-i-1]+[c]
                    lst3=[j for j in lst2 if j!=c]
                    lst3.sort()
                    lst4=lst1+lst3
                    break
            array=lst4
    out.append(' '.join(map(str,array)))
print('\n'.join(out))