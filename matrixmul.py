#matrix multiplication program
#input for matrix1
a=b=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        a[i][j]=int(input("enter element a%d%d:"%(i+1,j+1)))
#input for matrix2
for i in range(2):
    for j in range(2):
        b[i][j]=int(input("enter element b%d%d:"%(i+1,j+1)))

c=[[0,0],[0,0]]
#computing result matrix
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            c[i][j] += a[i][k]*b[k][j]
for i in range(len(c)):
    print(c[i])

