import math
while True:
    n = int(input())
    lst=[]
    if n == 0:
        break
    for i in range(n):
        a, b = map(int, input().split())
        if b < 0:
            continue
        time = math.ceil((4500 / a) * 3.6 + b)
        lst.append(time)
    print(min(lst))