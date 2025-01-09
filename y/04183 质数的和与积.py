def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num=int(input())
for i in range(num//2,1,-1):
    if prime(i) and prime(num-i):
        print(i*(num-i))
        break