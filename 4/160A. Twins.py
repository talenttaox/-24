n=int(input())
coin=list(map(int,input().split()))
coin.sort(reverse=True)
value=sum(coin)
sum=0
for i in range(n):
    sum+=coin[i]
    if sum*2>value:
        break
print(i+1)