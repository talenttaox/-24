for i in range(1,6):
    lst=[int(j) for j in input().split()]
    if 1 in lst:
        row=i
        col=lst.index(1)+1
        break
print(abs(row-3)+abs(col-3))