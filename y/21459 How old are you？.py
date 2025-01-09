num=int(input())
while num!=1:
    if num%2==0:
        a=num
        b=num//2
        print("{}/2={}".format(a,b))
        num=num//2
    else:
        a=num
        b=3*num+1
        print("{}*3+1={}".format(a,b))
        num=3*num+1
