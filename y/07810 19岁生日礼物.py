def a(num):
    if num%19==0:
        return True
    else:
        return False
def b(num):
    num=str(num)
    if '19' in num:
        return True
    else:
        return False

n=int(input())
for i in range(n):
    num=int(input())
    print('Yes' if a(num) or b(num) else 'No')