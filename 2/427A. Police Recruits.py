num=int(input())
lst=[int(i) for i in input().split()]
lst.append(1)
sum=0
k=0
for i in range(num):
    sum+=lst[i]
    if sum<0 and lst[i+1]>0:
        k-=sum
        sum=0
print(k)