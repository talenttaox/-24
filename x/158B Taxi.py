import math
n=int(input())
group=list(map(int,input().split()))
num1=group.count(1)
num2=group.count(2)
num3=group.count(3)
num4=group.count(4)
num=num4+math.ceil(num2/2)
if num1<=num3:
    num+=num3
else:
    if num2%2==1:
        num+=num3+math.ceil((num1-num3-2)/4)
    else:
        num+=num3+math.ceil((num1-num3)/4)
print(num)