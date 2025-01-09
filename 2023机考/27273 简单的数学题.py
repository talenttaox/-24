import math
t=int(input())
for i in range(t):
    n=int(input())
    k=int(math.log2(n))
    print((1+n)*n//2-2*(2**(k+1)-1))