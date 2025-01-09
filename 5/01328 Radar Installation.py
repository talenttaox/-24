import math
output=[]
s=1
while True:
    n,d=map(int,input().split())
    if n==d==0:
        break
    k=0
    distance=[]
    for i in range(n):
        x,y=map(int,input().split())
        if y>d:
            k=1
        a=math.sqrt(abs(d**2-y**2))
        distance.append([x-a,x+a])
    if k==1:
        output.append(f"Case {s}: -1")
    else:
        distance.sort(key=lambda x:x[1])
        j=0
        num=0
        while j<n:
            position=distance[j][1]
            num+=1
            while j<n and position>=distance[j][0]:
                    j+=1          
        output.append(f"Case {s}: {num}")
    s+=1
    input()
print('\n'.join(output))