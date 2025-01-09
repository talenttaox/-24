x,y=map(int,input().split())
lst=[1]*(x+1)
for i in range(y):
    a,b=map(int,input().split())
    lst[a:b+1]=[0]*(b-a+1)
num=lst.count(1)
print(num)
