n=int(input('Introduceti dimensiunile matricii:'))
matrix=[]
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
if n>1 and n<11:
    print('Elementele matritei',n,'x',n,':')
    for i in range(n):
        matrix.append(list(map(int, input().rstrip().split())))
    for i in range(n):
        a.append(matrix[i][i])
    a=sum(a)
    print('Suma diagonalei principale',a)
    for i in range(n):
        for j in range(n):
            if i+j==n-1:
                b.append(matrix[i][j])
    b=sum(b)
    print('Suma diagonalei secundare',b)
    for i in range(n):
        for j in range(n):
            if i<j:
                c.append(matrix[i][j])
    c=sum(c)
    print('Suma elementelor de deasupra diagonalei pricipala',c)
    for i in range(n):
        for j in range(n):
            if i>j:
                d.append(matrix[i][j])
    d=sum(d)
    print('Suma elementelor de sub diagonala principale',d)
    for i in range(n):
        for j in range(n):
            if i+j<n-1:
                e.append(matrix[i][j])
    e=sum(e)
    print('Suma elementelor de deasupra diagonalei secundare',e)
    for i in range(n):
        for j in range(n):
            if i+j>n-1:
                f.append(matrix[i][j])
    f=sum(f)
    print('Suma elementelor de sub diagonala secundara',f)
else:
    print('Dimensiunile matricii nu corespund cerintelor')    