row1, col1 = map(int, input().split())
matrix1 = []
for i in range(row1):
    matrix1.append([int(j) for j in input().split()])

row2, col2 = map(int, input().split())
matrix2 = []
for i in range(row2):
    matrix2.append([int(j) for j in input().split()])

row3, col3 = map(int, input().split())
matrix3 = []
for i in range(row3):
    matrix3.append([int(j) for j in input().split()])
    
if col1 == row2 and row1 == row3 and col2 == col3:
    result = []
    for i in range(row3):  
        temp = []
        for j in range(col2):  
            a = 0
            for k in range(col1):  
                a += matrix1[i][k] * matrix2[k][j]
            a += matrix3[i][j]
            temp.append(a)
        result.append(temp)
    
    for row in result:
        print(' '.join(map(str, row)))  
else:
    print("Error!")
