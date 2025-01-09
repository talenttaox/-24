array=list(map(int,input().split()))
num=0
minn=100000000
for i in array:
    minn=min(i,minn)
    num=max(num,i-minn)
print(num)