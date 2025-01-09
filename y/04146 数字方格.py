n=int(input())
sum=0
for i in range(0,n+1):
    a2=i
    for j in range(0,n+1):
        a1=j
        if (a1+a2)%2==0:
            for k in range(0,n+1):
                a3=k
                if (a2+a3)%3==0 and (a1+a2+a3)%5==0:
                    sum=max(sum,a1+a2+a3)
print(sum)