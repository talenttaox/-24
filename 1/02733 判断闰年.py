a = int(input())
if (a % 4 == 0 and a % 100!= 0 ) or (a % 400 == 0 and a % 3200!= 0):
    print("Y")
else:
    print("N")
