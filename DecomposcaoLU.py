def lu_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    P = [[float(i == j) for j in range(n)] for i in range(n)]

    for j in range(n):
        max_row = j
        for i in range(j + 1, n):
            if abs(A[i][j]) > abs(A[max_row][j]):
                max_row = i
        if max_row != j:
            A[j], A[max_row] = A[max_row], A[j]
            P[j], P[max_row] = P[max_row], P[j]

        for i in range(j + 1, n):
            L[i][j] = A[i][j] / A[j][j]
            for k in range(j + 1, n):
                A[i][k] -= L[i][j] * A[j][k]
            A[i][j] = 0

        U[j][j:] = A[j][j:]
        L[j][j] = 1

    return P, L, U


def imprime_matriz(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            print("%10.3f" % A[i][j], end="")
        print()
    print("-------------------")


A = [[1.0, -1.5, 1.5, 0.5], [-1.0, -4.5, 1.0, 2.0], [2.0, 1.0, 0.0, -3.0], [-2.0, 1.0, 1.5, 2.0]]

# Calculando a decomposição LU
P, L, U = lu_decomposition(A)

# Imprimindo os resultados
print("Matriz P:")
imprime_matriz(P)
print("Matriz L:")
imprime_matriz(L)
print("Matriz U:")
imprime_matriz(U)
