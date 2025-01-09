n=int(input())
list=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for i in range(1,n+1):
    date=input()
    year=int(date[0:4])
    m=int(date[4:6])
    if m<3:
        m+=12
        year-=1
    c=int(str(year)[0:2])
    y=int(str(year)[2:4])
    d=int(date[6:8])
    w=y+y//4+c//4-2*c+26*(m+1)//10+d-1
    num=w%7
    print(list[num])