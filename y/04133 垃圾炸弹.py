d=int(input())
n=int(input())
area=[[0]*1025 for i in range(1025)]
for _ in range(n):
    x,y,k=map(int,input().split())
    for i in range(max(x-d,0), min(x+d+1,1025)):
        for j in range(max(y-d,0), min(y+d+1,1025)):
            area[i][j]+=k
num=sum=0
for i in range(0,1025):
  for j in range(0,1025):
    if area[i][j]>sum:
      sum=area[i][j]
      num=1
    elif area[i][j]==sum:
      num+=1
print(num,sum)