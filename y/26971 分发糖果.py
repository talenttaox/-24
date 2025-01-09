n=int(input())
ratings=list(map(int,input().split()))
candy=[1]
for i in range(1,n):
    if ratings[i]>ratings[i-1]:
        candy.append(candy[-1]+1)
    #elif ratings[i]==ratings[i-1]:
        #candy.append(candy[-1])
    else:
        candy.append(1)
for i in range(n-2,-1,-1):
    if ratings[i+1]<ratings[i]:
        candy[i]=max(candy[i],candy[i+1]+1)
    #elif ratings[i]==ratings[i+1]:
        #candy[i]=candy[i+1]
print(sum(candy))
#print(candy)