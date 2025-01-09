h=int(input())
n=int(input())
time=2*h-n*0.5
num=0
lst=[]
for i in range(n):
    s,c=map(float,input().split())
    lst.append([s,c,s*c])
lst.sort(key=lambda x:x[2],reverse=True)
for i in range(len(lst)):
    if time>=5/lst[i][0]:
        num+=5*lst[i][1]
        time-=5/lst[i][0]
    else:
        num+=time*lst[i][0]*lst[i][1]
        break
print(f"{num:.1f}")