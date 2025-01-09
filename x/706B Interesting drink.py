n = int(input())
prices = sorted(list(map(int, input().split())))
q = int(input())
coins = [int(input()) for _ in range(q)]
dp = [0] * 100001
for price in prices:
    dp[price] += 1
for i in range(1, len(dp)):
    dp[i] += dp[i-1]
for coin in coins:
    if coin >= len(dp):
        print(dp[-1])
    else:
        print(dp[coin])