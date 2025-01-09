num=int(input())
num2=bin(num)[2:]
list=[i for i in num2]
list1=list[::-1]
if list==list1:
    print('Yes')
else:
    print('No')