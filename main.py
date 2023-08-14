A = [[1, 1, 1], [2, 1, -1], [1, 2, 3]]
b = [3, 2, 6]

k = 0
i = k + 1
n = 3
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
    k = k + 1

for i in range(n):
    for j in range(n):
        print("%10.5f" % A[i][j], end="")
    print("%20.2f" % b[i])
