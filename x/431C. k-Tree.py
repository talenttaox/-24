n,k,d=map(int,input().split())
mod = 10**9 + 7
A = [1] + [0] * n
B = [1] + [0] * n
for i in range(1, n + 1):
    for j in range(1, min(i,k)+1):
        A[i] = (A[i] + A[i - j]) % mod
    for j in range(1, min(d, i + 1)):
        B[i] = (B[i] + B[i - j]) % mod
print((A[n] - B[n]) % mod)