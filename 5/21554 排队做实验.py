n=int(input())
lst=list(map(int,input().split()))
lsta=[]
for i in range(1,n+1):
    lsta.append([lst[i-1],i])
lsta.sort(key=lambda x:x[0])
time=0
for i in range(n-1):
    time+=lsta[i][0]*(n-1-i)
time=time/n
out=[]
for i in range(n):
    out.append(lsta[i][1])
print(' '.join(map(str,out)))
print(f"{time:.2f}")