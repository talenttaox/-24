while True:
    n=int(input())
    if n==0:
        break
    hotels=[tuple(map(int,input().split())) for i in range(n)]
    hotels.sort(key=lambda x:(x[0],x[1]))
    num=1
    cost=hotels[0][1]
    for i in range(n):
        if hotels[i][1]<cost:
            num+=1
            cost=hotels[i][1]
    print(num)