def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num=int(input())
k=0
s=1
for i in range(2,num+1):
    if prime(i):
        if num%(i**2)==0:
            s=0
            break
        elif num%i==0:
            k+=1
if s==0:
    print(0)
else:
    print(1 if k%2==0 else -1)