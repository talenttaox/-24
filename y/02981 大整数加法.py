a=input()
a=a[::-1]
b=input()
b=b[::-1]
sum=''
k=0
if len(a)>len(b):
    b+='0'*(len(a)-len(b))
else:
    a+='0'*(len(b)-len(a))
for i in range(len(a)):
    if int(a[i])+int(b[i])+k>=10:
        sum+=str(int(a[i])+int(b[i])+k-10)
        k=1
    else:
        sum+=str(int(a[i])+int(b[i])+k)
        k=0
if k==1:
    sum+='1'
sum=sum[::-1]
print(int(sum))