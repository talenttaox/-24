import copy
def judge(s):
    room=copy.deepcopy(room0)
    light=[[0]*6 for i in range(5)] 
    for i in range(6):
        if s[i]=='1':
            light[0][i]=1
            for j in range(5):
                nx,ny=dx[j],i+dy[j]
                if 0<=nx<5 and 0<=ny<6:
                    room[nx][ny]=abs(1-room[nx][ny])
    for x in range(1,5):
        for y in range(6):
            if room[x-1][y]==1:
                light[x][y]=1
                for j in range(5):
                    nx,ny=x+dx[j],y+dy[j]
                    if 0<=nx<5 and 0<=ny<6:
                        room[nx][ny]=abs(1-room[nx][ny])
    for i in range(6):
        if room[-1][i]==1:
            return (False,light)
    return (True,light)
    

dx=[0,0,1,-1,0]
dy=[1,-1,0,0,0]



first=[]
for i in range(64):
    binn=int(bin(i)[2:])
    first.append(f"{binn:06d}")
room0=[]
for i in range(5):
    room0.append(list(map(int,input().split())))
for i in range(64):
    s=first[i]
    key,light=judge(s)
    if key:
        for j in light:
            print(' '.join(map(str,j)))
        break
