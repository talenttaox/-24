import math
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n =int(input())
if n<6 or n%2==1:
    print("Error!")
else:
    for i in range((n)//2+1):
        if prime(i) and prime(n-i):
            print(str(n)+"="+str(i)+"+"+str(n-i))