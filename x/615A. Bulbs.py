n,m=map(int,input().split())
list = [0 for i in range(m)]  
for i in range(n):
    list1=[int(a) for a in input().split()]
    for j in range(1,len(list1)):
        k=list1[j]
        if list[k-1]==0:
            list[k-1]=1
        else:
            list[k-1]=1
if 0 in list:
    print("NO")
else:
    print("YES")