n=int(input())
for i in range (n):
    length,num=map(int,input().split())
    lst=list(map(int,input().split()))
    lst1=[abs(i-length/2) for i in lst]
    lst1.sort()
    lst.sort()
    a=int(length/2-lst1[0])
    b=-lst[0]+lst[-1]+max(lst[0],length-lst[-1])
    print(a,b)