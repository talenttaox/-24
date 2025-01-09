from collections import deque

def bfs(n,m):
    queue=deque()
    visited=set()
    queue.append((n,0,''))
    visited.add(n)
    while queue:
        x,step,way=queue.popleft()
        if x==m:
            return way,step
        if x*3 not in visited:
            queue.append((x*3,step+1,way+'H'))
            visited.add(x*3)
        if x//2 not in visited:
            queue.append((x//2,step+1,way+'O'))
            visited.add(x//2)

while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    out,k=bfs(n,m)
    print(k)
    print(out)
    