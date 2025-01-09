import math
while True:
    lst=[int(i) for i in input().split()]
    k=0
    if lst.count(0)==6:
        break
    else:
        num6,num5,num4,num3,num2,num1=lst[5],lst[4],lst[3],lst[2],lst[1],lst[0]
        k=num6+num5+num4
        k+=math.ceil(num3/4)
        rest3=4-num3%4
        if rest3==1:
            if num2<=num4*5+1:
                pass
            else:
                k+=math.ceil((num2-num4*5-1)/9)
        elif rest3==2:
            if num2<=num4*5+3:
                pass
            else:
                k+=math.ceil((num2-num4*5-3)/9)
        elif rest3==3:
            if num2<=num4*5+5:
                pass
            else:
                k+=math.ceil((num2-num4*5-5)/9)
        elif rest3==4:
            if num2<=num4*5:
                pass
            else:
                k+=math.ceil((num2-num4*5)/9)
        if num1<=k*36-num6*36-num5*25-num4*16-num3*9-num2*4:
            pass
        else:
            k+=math.ceil((num1-k*36+num6*36+num5*25+num4*16+num3*9+num2*4)/36)
        print(k)