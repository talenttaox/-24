num=int(input())
for i in range(num):
    a=int(input())
    lst=[1]*a
    for j in range(1,a+1):
        for k in range(1,a+1):
            if k%j==0:
                lst[k-1]*=-1
    print(lst.count(-1)) 
