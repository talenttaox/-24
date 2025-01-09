n=int(input())
for i in range(n):
    num=int(input())
    if num==1:
        print(1)
    elif num==2:
        print(2)
    else:
        a,b = 1,2 
        for j in range(3,num+1):
            a,b =b,(b*2+a)%32767 
        print(b)