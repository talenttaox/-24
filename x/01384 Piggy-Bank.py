t=int(input())
output=[]
for _ in range(t):
    coin=[]
    e,f=map(int,input().split())
    n=int(input())
    for j in range(n):
        coin.append(list(map(int,input().split())))
    dp=[float('inf')]*(f-e+1)
    dp[0]=0
    for i in range(n):
        for j in range(coin[i][1],f-e+1):
            dp[j]=min(dp[j],dp[j-coin[i][1]]+coin[i][0])
    if dp[-1]==float('inf'):
        output.append('This is impossible.')
    else:
        output.append('The minimum amount of money in the piggy-bank is {}.'.format(dp[-1]))
print('\n'.join(output))