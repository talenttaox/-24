list1=[int(item) for item in input().split()]
if list1[0]%2==0 or list1[1]%2==0:
    print(list1[0]*list1[1]//2)
else:
    print((list1[0]*list1[1]-1)//2)