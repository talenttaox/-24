t=int(input())
output=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=sorted(list(zip(a,b)),reverse=True)
    time=0
    for i in range(n):
        time+=c[i][1]
        if time>=c[i][0]:
            time=max(c[i][0],time-c[i][1])
            break
    output.append(time)
print('\n'.join(map(str,output)))