d=[0]*13
f=[float('inf')]*13
d[1]=1
for i in range(2,13):
    d[i]=d[i-1]*2+1
f[1]=1
for i in range(2,13):
    for j in range(1,i):
        f[i]=min(f[i],2*f[i-j]+d[j])
for i in range(1,13):
    print(f[i])