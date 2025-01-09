n=int(input())
for i in range(n):
    angle=float(input())
    if 360%(180-angle)==0:
        print("YES")
    else:
        print("NO")