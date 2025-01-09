import math
def fortune(x):
    judge=1
    for i in str(x):
        if i not in "47":
            judge*=0
    if judge==1:
        return  True
    else:
        return False
num=int(input())
lst=[]
for i in range(1,num+1):
    if fortune(i):
        lst.append(i)
for i in lst:
    if num%i==0 :
        print("YES")
        break
else:
    print("NO")