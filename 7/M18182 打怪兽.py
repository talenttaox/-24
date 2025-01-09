num=int(input())
output=[]
for _ in range(num):
    skill=[]
    n,m,b=map(int,input().split())
    for i in range(n):
        t,x=map(int,input().split())
        skill.append((t,-x))
    skill.sort(key=lambda x:(x[0],x[1]))
    time=0
    k=0
    for i in range(n):
        if skill[i][0]==time:
            if k<m:
                k+=1
                b+=skill[i][1]
        else:
            time=skill[i][0]
            b+=skill[i][1]
            k=1
        if b<=0:
            output.append(skill[i][0])
            break
        if i==n-1 and b>0:
            output.append('alive')
            break
print('\n'.join(map(str,output)))
