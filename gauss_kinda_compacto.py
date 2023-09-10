from colorama import init, Fore, Style


def printar(A, b):
    n = len(A)
    for i in range(n):
        for j in range(n):
            print(Fore.BLUE + "%10.3f" % A[i][j] + Style.RESET_ALL, end="")
        if b is not None:
            print(Fore.MAGENTA + "%20.5f" % b[i] + Style.RESET_ALL)
        print()
    print("-------------------")


def gauss_compacto(A, b, n, op):
    k = 0  # colunas
    x = [0 for _ in range(n)]

    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    P = [[float(i == j) for j in range(n)] for i in range(n)]

    # Eliminação de Gauss
    while k < n:
        indice_max = k
        for i in range(k + 1, n):  # pivoteamento parcial
            if abs(A[i][k]) > abs(A[indice_max][k]):
                indice_max = i
        if indice_max > k:
            for j in range(k, n):
                A[k][j], A[indice_max][j] = A[indice_max][j], A[k][j]
            for m in range(n):
                L[k][m], L[indice_max][m] = L[indice_max][m], L[k][m]

            P[k], P[indice_max] = P[indice_max], P[k]
            b[k], b[indice_max] = b[indice_max], b[k]

        printar(A, b)

        for i in range(k + 1, n):  # escalonamento
            mult = A[i][k] / A[k][k]
            L[i][k] = mult
            A[i][k] = mult
            for j in range(k, n):
                A[i][j] = A[i][j] - mult * A[k][j]
            b[i] = b[i] - mult * b[k]

        U[k][k:] = A[k][k:]
        L[k][k] = 1
        k = k + 1


    # Resolução do sistema
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += A[i][j] * x[j]
        x[i] = (b[i] - soma) / A[i][i]


    return x, L, U, P


def le_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        valores = input(f"Digite os valores da linha {i + 1} separados por espaco: ")
        valores_split = [float(element) for element in valores.split(" ")]
        if len(valores_split) != colunas:
            print(f"Devem ser inseridos {colunas} valores por linha!")
            return None
        matriz.append(valores_split)
    return matriz


def le_vetor(linhas):
    valores = input(f"Digite os valores do vetor separados por espaco: ")
    valores_split = [float(element) for element in valores.split(" ")]
    if len(valores_split) != linhas:
        print(f"Devem ser inseridos {linhas} valores!")
        return None

    return valores_split


def personalizada():
    n = int(input("Digite a ordem da matriz A: "))
    print("Preencha os valores da matriz A:")
    A = le_matriz(n, n)
    print("\nPreencha os valores do vetor b:")
    b = le_vetor(n)

    return n, A, b


def main():
    # Inicializa o módulo colorama
    init()

    op = None

    while op not in ["1", "2", "3"]:
        print("Olá, digite a opção desejada:")
        print("1- Usar um exemplo personalizado")
        print("2- Usar um exemplo de matriz 3x3")
        print("3- Usar um exemplo de matriz 4x4")
        op = input("\nOpção: ")

        if op not in ["1", "2", "3"]:
            print("OPÇÃO INVÁLIDA")

    if op == "1":  # Exemplo matriz personalizada
        n, A, b = personalizada()
    elif op == "2":  # Exemplo matriz 3x3
        n = 3
        A = [[3, -4, 1], [1, 2, 2], [4, 0, -3]]
        b = [9, 3, -2]
        # Resposta = x = 1.0 -1.0 2.0
    elif op == "3":  # Exemplo matriz 4x4
        n = 4
        A = [[1, 1, 1, 1], [1, -1, -1, -1], [-1, 1, -1, -1], [-1, -1, 1, -1]]
        b = [11, -9, -7, -5]
        # Resposta = x = 1.0 2.0 3.0 5.0

    # op = None
    # while op not in ["1", "2"]:
    #     print("Por qual método deseja solucionar o sistema:")
    #     print("1- Regressão linear")
    #     print("2- LUx")
    #     op = input("\nOpção: ")
    #
    #     if op not in ["1", "2"]:
    #         print("OPÇÃO INVÁLIDA")

    x, L, U, P = gauss_compacto(A, b, n, op)
    print("Resultado do sistema: ")
    for i in x:
        print("%5.5f " % i, end="")

    # Mostrando A, L, U e P
    print("\n\nMatriz A:")
    printar(A, None)
    print("Matriz L:")
    printar(L, None)
    print("Matriz U:")
    printar(U, None)
    print("Matriz P:")
    printar(P, None)


if __name__ == '__main__':
    main()
