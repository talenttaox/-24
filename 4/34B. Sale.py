n,m=map(int,input().split())
tv=list(map(int,input().split()))
tv.sort()
num=0
for i in range(m):
    if tv[i]>0:
        break
    num-=tv[i]
print(num)