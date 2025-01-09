a=input()
list=[]
list1=[]
for i in a:
    list.append(i.lower())
for i in range(len(list)):
    if list[i] in ["a","e","i","o","u","y"]:
        list1.append(i)    
    else:
        list[i]="."+list[i]
k=0       
for i in list1:
    list.pop(i-k)
    k+=1
str=""
for i in list:
    str+=i
print(str)
