n=int(input())
lst=[]
for i in range(n):
    row=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    lst.append(min(min(a)*row+sum(b),min(b)*row+sum(a)))
for i in lst:
    print(i)