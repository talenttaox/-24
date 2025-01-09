num=int(input())
list=[int(i) for i in input().split()]
a=[]
sum=1
if num==1:
    print(1)
else:
    for i in range(num-1):
        if i==num-2 and list[i]<=list[i+1]:
            sum+=1
            a.append(sum)
        elif list[i]<=list[i+1]:
            sum+=1
        else:
            a.append(sum)
            sum=1
    print(max(a))