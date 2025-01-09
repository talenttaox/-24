num=int(input())
a=b=0
if num%2==0:
  a=num//2
  b=num//4+(num%4)//2
print(b,a)