from collections import deque
def bfs(start,end,maze):
    q=deque([start])
    inq=set()
    ans=[]
    while q:
        seg,(x0,y0),dir=q.popleft()
        if (x0,y0)==end:
            ans.append(seg)
            break
        for i in range(4):
            x=x0+dx[i]
            y=y0+dy[i]
            if 0 <=x<w+2 and 0<=y< h+2 and ((x,y,i) not in inq):
                new_dir=i
                new_seg=seg if new_dir==dir else seg+1
                if (x,y)==end:
                    ans.append(new_seg)
                    continue
                if maze[y][x]!='X':
                    inq.add((x,y,i))
                    q.append((new_seg,(x,y),new_dir))

    if len(ans)==0:
        return -1
    else:
        return min(ans)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
s=1

while True:
    w,h=map(int,input().split())
    if w==h==0:
        break
    print('Board #{}:'.format(s))
    maze=[' '*(w+2)]+[' '+input()+' ' for _ in range(h)]+[' '*(w+2)]
    n=1
    while True:
        x1,y1,x2,y2=map(int,input().split())
        if x1==x2==y1==y2==0:
            break
        start = (0,(x1, y1), -1)
        end = (x2, y2)
        num=bfs(start,end,maze)
        if num>0:
            print('Pair {}: {} segments.'.format(n,num))
        else:
            print('Pair {}: impossible.'.format(n))
        n+=1
    print()
    s+=1


