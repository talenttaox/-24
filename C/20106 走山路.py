import heapq
def dijkstra(start,end,hill):
    consume=[[float('inf')]*n for _ in range(m)]
    x0,y0=start
    xe,ye=end
    if hill[x0][y0]=='#' or hill[xe][ye]=='#':
        return 'NO'
    consume[x0][y0]=0
    pq=[(0,x0,y0)]
    while pq:
        con,x,y=heapq.heappop(pq)
        if (x,y)==end:
            return con
        for i in range(4):
            x1=x+dx[i]
            y1=y+dy[i]
            if 0<=x1<m and 0<=y1<n and hill[x1][y1]!='#':
                con1=con+abs(int(hill[x][y])-int(hill[x1][y1]))
                if con1<consume[x1][y1]:
                    consume[x1][y1]=con1
                    heapq.heappush(pq,(con1,x1,y1))
    return 'NO'

m,n,p=map(int,input().split())
hill=[]
for i in range(m):
    hill.append(list(map(str,input().split())))
dx=[0,0,1,-1]
dy=[1,-1,0,0] 
out=[]
for i in range(p):
    a,b,c,d=map(int,input().split())
    print(dijkstra((a,b),(c,d),hill))