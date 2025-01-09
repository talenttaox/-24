def f(string):
    if string=='':
        return 0
    else:
        return int(string)
m=int(input())
n=int(input())
number=input().split()
for i in range(n):
    for j in range(n-1-i):
        if number[j] + number[j+1] > number[j+1] + number[j]:
            number[j],number[j+1] = number[j+1],number[j]
length=[]
for num in number:
    length.append(len(num))
dp=[['']*(m+1) for _ in range(n+1)]
for k in range(m+1):
    dp[0][k]=''
for l in range(n+1):
    dp[l][0]=''
for i in range(1,n+1):
    for j in range(1,m+1):
        if length[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=str(max(f(dp[i-1][j]),int(number[i-1]+dp[i-1][j-length[i-1]])))
print(dp[n][m])