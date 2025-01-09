stra=''
num=0
sum=0
lsta=[]
for i in range(1,33000):
    stra+=str(i)
    num+=len(str(i))
    sum+=num
    lsta.append(sum)
n=int(input())
for i in range(n):
    a=int(input())
    if a==1:
        print(1)
    else:
        for j in range(len(lsta)):
            if a<=lsta[j]:
                k=a-1-lsta[j-1]
                print(stra[k])
                break