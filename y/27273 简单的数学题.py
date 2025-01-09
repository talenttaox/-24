import math
a=int(input())
for i in range(a):
    a=int(input())
    sum=(1+a)*a//2
    num=int(math.log2(a))
    for j in range(num+1):
        sum-=2*(2**j)
    print(sum)
