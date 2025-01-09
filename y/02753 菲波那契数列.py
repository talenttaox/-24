num=int(input())
lst=[1,1]
for i in range(num):
    index=int(input())
    if index<=len(lst):
        print(lst[index-1])
    else:
        for j in range(index-len(lst)):
            lst.append(lst[-1]+lst[-2])
        print(lst[index-1])