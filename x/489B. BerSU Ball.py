import math
boy=int(input())
boy_skill=list(map(int,input().split()))
boy_skill.sort()
girl=int(input())
girl_skill=list(map(int,input().split()))
girl_skill.sort()
if boy<=girl:
    lst1=boy_skill
    lst2=girl_skill
else:
    lst1=girl_skill
    lst2=boy_skill
result=0
k=0
for i in range(len(lst1)):
    for j in range(k,len(lst2)):
        if abs(lst1[i]-lst2[j])<=1:
            result+=1
            k=j+1
            break
print(result)