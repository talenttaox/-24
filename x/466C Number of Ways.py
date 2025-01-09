n=int(input())
array=list(map(int,input().split()))
a=sum(array)
if a%3!=0:
    print(0)
else:
    num=0
    total=0
    k=0
    b1=a//3
    b2=2*b1
    for i in range(n-1):
        total+=array[i]
        if total==b2:
            num+=k
        if total==b1:
            k+=1
    print(num)