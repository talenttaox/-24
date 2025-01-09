n=int(input())
a,b=map(int,input().split())
array=[]
ans=0
for i in range(n):
    array.append(list(map(int,input().split())))
array.sort(key=lambda x:(x[0]*x[1]))
for i in range(n):
    ans=max(ans,a//array[i][1])
    a=a*array[i][0]
print(ans)