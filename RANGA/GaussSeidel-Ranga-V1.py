import math

# Para entrar com a dimensao da matrix A
n = 5
tolerance = 0.00001
teste = 1

print()
print("\33[134m*******************************\33[m")
print("Este programa é para resolver um sistema Ax = b ")
print("  pelo método iterativo de Gauss-Seidel.")
#
print()
print("Opção: \33[134m0\33[m para entrar os valores da uma matriz")
print("Opção: \33[134m1\33[m para usar um exemplo de matriz 3x3 pronto")
print("Opção: \33[134m2\33[m para usar um exemplo de matriz 4x4 pronto")
print()
opt = int(input("Entrar com o valor da opção: "))
#
if opt == 0:
    # Exemplo para digitar
    print()
    print()
    n = int(input("Digitar a dimensao n da matriz A: "))
#
# Para inicializar a matriz A e o vetor v
A = []
B = []
x = []
y = []
b = []
c = []
for i in range(0, n + 1):
    x.append(0.0)
    y.append(0.0)
    b.append(0.0)
    c.append(0.0)
    A.append([])
    B.append([])
    for j in range(0, n + 1):
        A[i].append(0.0)
        B[i].append(0.0)
#
if opt == 0:
    #:::: Para entrar com os valores de A[i,j]
    for i in range(1, n + 1):  # i varia de 1 para n
        for j in range(1, n + 1):  # j varia de 1 para n
            print("Digitar o valor de A[%1d,%1d]:" % (i, j), end=' ')
            # A[i][j] = float(input())
            TTT = input()
            A[i][j] = float(TTT)
else:
    if opt == 1:
        # Exemplo pronto de uma matriz 3 x 3.
        n = 3
        A[1][1] = 4.0
        A[1][2] = 1.0
        A[1][3] = -1.0
        A[2][1] = 1.0
        A[2][2] = 5.0
        A[2][3] = 1.0
        A[3][1] = -1.0
        A[3][2] = 1.0
        A[3][3] = 2.0
    else:
        # Exemplo pronto de uma matriz 4 x 4 definida positiva.
        if opt == 2:
            n = 4
            A[1][1] = 4.0
            A[1][2] = 1.0
            A[1][3] = 0.0
            A[1][4] = -1.0
            A[2][1] = 1.0
            A[2][2] = 8.0
            A[2][3] = 2.0
            A[2][4] = 1.0
            A[3][1] = 0.0
            A[3][2] = 2.0
            A[3][3] = 4.0
            A[3][4] = 1.0
            A[4][1] = -1.0
            A[4][2] = 1.0
            A[4][3] = 1.0
            A[4][4] = 6.0
# 
#:: Imprimir a Matriz inicial 
print()
print("           A = ")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("%9.4f" % A[i][j], end='')
    print()
print()
#::::
#:: Para entrar com os valores de b[i]
print("Entrar com os valores do vetor b:")
print("Obs.: Se b= i-ésima coluna da matriz I, ")
print("         então x= i-ésima coluna de A^(-1). ")
print()
#
for i in range(1, n + 1):
    print("Digitar o valor de b[%1d] =" % i, end=' '),
    b[i] = float(input())
#
for i in range(1, n + 1):
    for j in range(1, i):
        B[i][j] = - A[i][j] / A[i][i]
    for j in range(i + 1, n + 1):
        B[i][j] = - A[i][j] / A[i][i]
    c[i] = b[i] / A[i][i]
#
#:: Matriz B e vetor c
print(end="A matriz \33[034mB\33[m e vetor \33[032mc\33[m no ")
print("sistem x = Bx + c")
#
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("\33[0;34m%10.6f" % B[i][j], end='')
    print(" \33[0;32m%10.6f" % c[i], "\33[m")
    # print()
print()
#::::
#:: Para entrar com os valores iniciais   
print("Entrar com o vetor inicial: ")
for i in range(1, n + 1):
    print("Digitar o valor de x[%1d] =" % i, end=' '),
    x[i] = float(input())
# 
k = 0
while teste > 0:
    dif = 0.0
    for i in range(1, n + 1):
        ss = 0.0
        for j in range(1, i):
            ss = ss + B[i][j] * y[j]
        for j in range(i + 1, n + 1):
            ss = ss + B[i][j] * x[j]
        y[i] = c[i] + ss
        dif = dif + abs(y[i] - x[i])
    k = k + 1
    if dif < tolerance: teste = 0
    print("%2d" % k, end='')
    for i in range(1, n + 1):
        x[i] = y[i]
        print("%12.7f" % x[i], end='')
    print()
#::: Imprimir resultado final  
print()
for i in range(1, n + 1):
    print("  x[%1d] =" % i, "%12.6f" % x[i])
print()
