def sgn(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    elif x < 0:
        return -1
n = int(input())
lst = list(map(int,input().split()))
sgna = [sgn(lst[i+1]-lst[i]) for i in range(n-1)]

s = 1
pre = 0
for i in range(n-1):
    if sgna[i] * pre < 0 or (pre == 0 and sgna[i] != 0):
        s += 1
        pre = sgna[i]
print(s)