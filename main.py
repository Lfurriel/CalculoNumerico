import copy

A = [[1.0, -1.5, 1.5, 0.5], [-1.0, -4.5, 1.0, 2.0], [2.0, 1.0, 0.0, -3.0], [-2.0, 1.0, 1.5, 2.0]]
B = copy.deepcopy(A)
b = [1, 0, 0]
x = []
k = 0
i = k + 1
n = 4


U = [[]for i in range(4)]
L = [[]for i in range(4)]

while k < n:

    maior = k
    for i in range(k + 1, n):
        if abs(A[i][k]) > abs(A[maior][k]):
            maior = i
    if maior > k:
        for j in range(k, n):
            aux = A[k][j]
            A[k][j] = A[maior][j]
            A[maior][j] = aux
        aux = b[k]
        b[k] = b[maior]
        b[maior] = b[k]

    for i in range(k + 1, n):
        mult = A[i][k] / A[k][k]
        for j in range(k, n):
            A[i][j] = A[i][j] - mult * A[k][j]
        b[i] = b[i] - mult * b[k]
        U[i][j] = mult

    k = k + 1

for i in range(n - 1, -1, -1):
    soma = 0
    for j in range(i + 1, n):
        soma -= (A[i][j] * x[i - 1]) / A[i][i]
    soma += b[i] / A[i][i]
    x.append(soma)

for i in range(n):
    for j in range(n):
        print("%10.5f" % A[i][j], end="")
    print("%20.2f" % b[i])

for i in range(n):
    print("%10.2f" % x[i])

k = 1
for j in range(0, n):
    U[1][j] = A[1][j]
for i in range(1, n):
    L[i][1] = A[i][1] / U[1][1]

for k in range(1, n - 1):
    for j in range(k, n):
        sj = 0.0
        for ir in range(0, k - 1):
            sj = sj + L[k][ir] * U[ir][j]
        U[k][j] = A[k][j] - sj
    for i in range(k, n):
        si = 0.0
        for ir in range(0, k):
            si = si + L[i][ir] * U[ir][k]
        L[k][j] = (A[i][k] - si)/U[k][k]
    sj = 0
    for ir in range(0, n):
        sj = sj + L[n-1][ir] * U[ir][n-1]
    U[n-1][n-1] = A[n-1][n-1] - sj