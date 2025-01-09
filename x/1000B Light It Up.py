n,m=map(int,input().split())
time=[0]+list(map(int,input().split()))+[m]
total=0
output=0
for i in range(1,len(time),2):
    total+=time[i]-time[i-1]
output=total
sum_time=0
for i in range(2,len(time),2):
    sum_time+=time[i-1]-time[i-2]
    if time[i]>time[i-1]+1:
        output=max(output,2*sum_time+m-total-time[i-1]-1)
print(output)
