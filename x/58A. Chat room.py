world="hello"
index=0
s=input()
for i in s:
    if i==world[index]:
        index+=1
    if index==len(world):
        print("YES")
        break
else:
    print("NO")