n = int(input())
lst1 = []
lst2 = []
lst = []
for i in range(n):
    id, age = map(str, input().split())
    if int(age) >= 60:
        lst1.append([id,int(age),1000-i])
    else:
        lst2.append([id,age])
lst1.sort(key=lambda x: (x[1],x[2]), reverse=True)
for i in lst1:
    lst.append(i[0])
for i in lst2:
    lst.append(i[0])
for i in lst:
    print(i)