def dfs(a,b):
    global n
    a0=max(a,b)
    b0=min(a,b)
    if b==0 or a0//b0>=2 or a0==b0:
        return n
    else:
        n+=1
        a1=b0
        b1=a0-b0
        dfs(a1,b1)

while True:
    a,b=map(int,input().split())
    n=0
    if a==0 and b==0:
        break
    dfs(a,b)
    print('win' if n%2==0 else 'lose')
