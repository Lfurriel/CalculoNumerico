def gauss_compacto(A, b):
    n = len(b)

    # Eliminação Gaussiana
    for i in range(n):
        for j in range(i + 1, n):
            m = A[j][i] / A[i][i]
            b[j] -= m * b[i]
            for k in range(i, n):
                A[j][k] -= m * A[i][k]

    # Substituição Regressiva
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i, n))
        x[i] = (b[i] - s) / A[i][i]

    return x


A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]

x = gauss_compacto(A, b)
print(x)
