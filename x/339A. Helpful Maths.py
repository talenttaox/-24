list=[i for i in input().split("+")]
list.sort()
str=""
for i in range(len(list)-1):
    str=str+list[i]+"+"
str=str+list[-1]
print(str)