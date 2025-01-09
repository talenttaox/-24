n = 1000000
a = [1]*n
s = set()
input()
nums = [int(x) for x in input().split()]
for i in range(2, n):
    if a[i]:
        s.add(i*i)
        for j in range(i*i, n, i):
            a[j] = 0
for x in nums:
    if x in s:
        print('YES')
    else: 
        print('NO')