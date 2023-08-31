import math
# Para entrar com a dimensao da matrix A
n = 6; tolerance = 0.0000001;  teste = 1 

print()
print("*******************************")
print("Este programa é para resolver um sistema Ax = b ")
print("  pelo método Gauss-Compacto.")
print("A primeira parte do programa converte a matrix A")
print("  em duas matrizes \33[0;34mL\33[m e \33[0;32mU\33[m talque: LU = PA. ")
#
print()
print("Opção 0: para digitar valores de uma matriz")
print("Opção 1: para usar um exemplo de matriz 3x3 pronto")
print("Opção 2: para usar um exemplo de matriz 4x4 pronto")
print("Opção 3: para usar um outro exemplo de matriz 4x4 pronto")
print() 
opt = int(input("Entrar com o valor da opção: "))
#
if opt == 0: 
  # Exemplo para digitar
  print(); print(); 
  n = int(input("Digitar a dimensao n da matriz A: "))  
#
# Para inicializar a matriz A e o vetor v
A = [ ]; G = [ ];   v = [ ];  
for i in range(0,n+1):
  v.append(i); A.append([ ])  
  G.append([ ])
  for j in range(0,n+1):
    A[i].append(0.0)
    G[i].append(0.0)
if opt == 0: 
  #:::: Para entrar com os valores de A[i,j]
  for i in range (1,n+1): # i varia de 1 para n
    for j in range (1, n+1): # j varia de 1 para n
      print("Digitar o valor de A[%1d,%1d]:"%(i,j), end = ' ')
      #A[i][j] = float(input())
      TTT = input()
      A[i][j] = float(TTT)
else:
  # Exemplo pronto de uma matriz 3 x 3.
  if opt == 1:  
    n = 3
    #:::: Para entrar com os valores de A[i,j]
    A[1][1] = 4.0;  A[1][2] = 1.0; A[1][3] = -1.0; 
    A[2][1] = 1.0;  A[2][2] = 5.0; A[2][3] = 1.0; 
    A[3][1] = -1.0;  A[3][2] = 1.0; A[3][3] = 2.0; 
#
  else: 
    # Exemplo pronto de uma matriz 4 x 4.
    if opt == 2: 
      n = 4
    #:::: Para entrar com os valores de A[i,j]
      A[1][1] = 4.0;  A[1][2] = 1.0; A[1][3] = 0.0; A[1][4] = -1.0;
      A[2][1] = 1.0;  A[2][2] = 8.0; A[2][3] = 2.0; A[2][4] = 1.0;
      A[3][1] = 0.0;  A[3][2] = 2.0; A[3][3] = 4.0; A[3][4] = 1.0;
      A[4][1] = -1.0;  A[4][2] = 1.0; A[4][3] = 1.0; A[4][4] = 6.0; # 
    # Exemplo pronto de uma matriz 4 x 4. 
    else: 
      n = 4
   #:::: Para entrar com os valores de A[i,j]   
      A[1][1] = 2.0;  A[1][2] = 1.0; A[1][3] = -1.0; A[1][4] = -1.0;
      A[2][1] = 1.0;  A[2][2] = 2.0; A[2][3] = 2.0; A[2][4] = 1.0;
      A[3][1] = -1.0;  A[3][2] = 2.0; A[3][3] = 4.0; A[3][4] = 1.0;
      A[4][1] = -1.0;  A[4][2] = 1.0; A[4][3] = 1.0; A[4][4] = 6.0; # 
# 
#:: Imprimir a Matriz inicial 
print("A = "); 
for i in range (1,n+1): 
  for j in range (1, n+1):
    print("%10.5f" % A[i][j], end = ' ')
  print()   
#:::: 
#:   Inicio do processo A -> LU
#::::
ut = 1
#
k = 1
val = A[k][k]
if val > 0: 
  G[k][k] = math.sqrt(val)
  print("G[",k,k, "]*G[",k,k, "] =", val)
else: 
  teste = -k
while teste > 0:
  for i in range(k+1,n+1):
    ss = 0.0
    for j in range(1,k):
      ss = ss + G[k][j]*G[i][j]
    G[i][k] = (A[i][k] - ss)/G[k][k]
  k = k+1 
  ss = 0.0   
  for j in range(1,k):
    ss = ss + G[k][j]*G[k][j]
  val = A[k][k] - ss
  if val > 0: 
    G[k][k] = math.sqrt(val)
    print("G[",k,k, "]*G[",k,k, "] =", val) 
    if k == n: 
      teste = 0
  else: 
    teste = -k
#
if teste == 0:
  print(); print("G = "); 
  for i in range (1,n+1): 
    for j in range(1,i+1):
      print("\33[0;34m%10.5f" % G[i][j], end = ' ')
    print("\33[m")   
else: 
  mm = -teste
  print("G[",mm,mm, "]*G[",mm,mm, "] =", val, " é negativo") 
  print("           A matriz nao é definida positiva")
#:::: 
# 
if teste == 0:
  print()
  Det = float(ut)
  for i in range(1,n+1):
    Det = Det*G[i][i]*G[i][i]
  print()
  print("Valor de determinante =%10.4f"%Det, end = ' '); 
#
if teste == 0:
  #
  print(); print()
  pp1 = input("Quer resolver Ax=b (sim = s)? ")    
  #:::: Para resolver o sistema Ax = b
  #:: Para inicializar os vetores b e x
  b = [ ]; x = [ ]; y = [ ]
  for i in range(0,n+1):
    b.append(0.0)
    x.append(0.0)
    y.append(0.0)
  #:: Para entrar com os valores de b[i]
  while pp1 == "s": 
    print()    
    print("Observação: Se b = i-ésima coluna da matriz identidade, ")
    print("            então x = i-ésima coluna de A^(-1). "); print()
    #
    for i in range(1,n+1):
      print("Digitar o valor de b[%1d] ="%i, end = ' '),
      b[i] = float(input())
    #
    #::: Para resolver o sistema Ly = b
    print() 
    print("Temos G Gt x = A x = b  e")
    #::: impressao do sistema Gy = b
    print(); print("Resolução do sistema Gy = b.")
    for j in range(1,n+1):
      print(end = '          ')
    print("\33[mb\33[m") 
    for i in range(1,n+1): 
      for j in range(1,i+1):
        print("\33[0;34m %8.5f" % G[i][j], end = '')
      for j in range(i+1,n+1):
        print(end = '         ')
      print("\33[m%7.3f" %b[i])
    #::: resolucao do sistema Gy = b
    y[1] = b[1]/G[1][1]
    for i in range(2, n+1): # i varia de 2 para n
      sum = 0.0
      for j in range(1,i): # j varia de 1 para i-1
        sum = sum + y[j]*G[i][j]
      y[i] = (b[i] - sum)/G[i][i]
    print()
    #
    #::: Para resolver o sistema Gt x = y
    #::: Impressão o sistema Gt x = y
    print(end = "Resolução do sistema Gt x = y.")
    print()
    for i in range(1,n+1):
      for j in range(1,i):
        print(end = '         ')
      for j in range(i,n+1):
        print("\33[0;32m %8.5f" % G[j][i], end = '')
      print("\33[m %12.6f" % y[i])
    #::: Resolucao do sistema Ux = y    
    x[n] = y[n]/G[n][n]
    for i in range(n-1, 0,-1): # i varia de n-1 para 1
      sum = 0.0
      for j in range(i+1,n+1): # j varia de i+1 para n
        sum = sum + x[j]*G[j][i]
      x[i] = (y[i] - sum)/G[i][i]
  
    #::: Imprimir resultado final  
    print()
    for i in range(1,n+1):
      print("  x[%1d] ="%i,"%12.6f" %x[i])
    print()
    pp1 = input("Quer resolver Ax=b de novo (sim = s)? ")
    #
else: 
  print(); 
  print("Sistema mal condicionado")