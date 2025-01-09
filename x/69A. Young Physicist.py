n=int(input())
list=[0]*3
for i in range(n):
    list_i=[a for a in input().split()]
    for j in range(3):
        list[j]+=int(list_i[j])
if list.count(0)==3:
    print("YES")
else:
    print("NO")