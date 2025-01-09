squares = set()
i = 1
while i * i <= 10**9:
    squares.add(str(i * i))
    i += 1

def dfs(num):
    global judge
    for i in range(1,len(num)+1):
        num1=num[:i]
        if num1 in squares:
            if num1==num:
                judge=True
            else:
                num2=num[i:]
                dfs(num2)

            

num=input()
judge=False
dfs(num)
print('Yes' if judge else 'No')