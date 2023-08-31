
# Para entrar com a dimensao da matrix A
n = 6; tolerance = 0.0000001;  teste = 0. 

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
A = [ ]; L = [ ];  U = [ ];  v = [ ];  
for i in range(0,n+1):
  v.append(i); A.append([ ])  
  L.append([ ]); U.append([ ])
  for j in range(0,n+1):
    A[i].append(0.0)
    L[i].append(0.0);   U[i].append(0.0);
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
    A[1][1] = 1.0;  A[1][2] = 1.0; A[1][3] = 1.0; 
    A[2][1] = -3.5;  A[2][2] = 2.0; A[2][3] = 1.0; 
    A[3][1] = 1.5;  A[3][2] = 2.0; A[3][3] = -1.0; 
#
  else: 
    # Exemplo pronto de uma matriz 4 x 4.
    if opt == 2: 
      n = 4
    #:::: Para entrar com os valores de A[i,j]
      A[1][1] = 2.0;  A[1][2] = 1.0; A[1][3] = 0.0; A[1][4] = -3.0;
      A[2][1] = 1.0;  A[2][2] = -1.5; A[2][3] = -7.5; A[2][4] = 0.5;
      A[3][1] = -2.0;  A[3][2] = 1.0; A[3][3] = 1.5; A[3][4] = 2.0;
      A[4][1] = -1.0;  A[4][2] = -4.5; A[4][3] = 1.0; A[4][4] = 1.5; # 
    # Exemplo pronto de uma matriz 4 x 4. 
    else: 
      n = 4
   #:::: Para entrar com os valores de A[i,j]   
      A[1][1] = 1.0;  A[1][2] = -1.5; A[1][3] = 1.5; A[1][4] = 0.5;
      A[2][1] = -1.0;  A[2][2] = -4.5; A[2][3] = 1.0; A[2][4] = 2.0;
      A[3][1] = 2.0;  A[3][2] = 1.0; A[3][3] = 0.0; A[3][4] = -3.0;
      A[4][1] = -2.0;  A[4][2] = 1.0; A[4][3] = 1.5; A[4][4] = 2.0; #       
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
for j in range(1,n+1):
  U[1][j] = A[1][j];
for i in range(2, n+1):
  L[i][1] = A[i][1]/U[1][1]
#
for k in range(2,n): 
  for j in range(k,n+1):
    sj = 0.0
    for ir in range(1, k):
      sj = sj + L[k][ir]*U[ir][j]
    U[k][j] = A[k][j] - sj
  for i in range(k+1,n+1):  
    si = 0.0
    for ir in range(1,k): 
      si = si + L[i][ir]*U[ir][k]
    L[i][k] = (A[i][k] - si)/U[k][k]
sj = 0.0
for ir in range(1,n):
  sj = sj + L[n][ir]*U[ir][n]
U[n][n] = A[n][n] - sj

print(); print("L = "); 
for i in range (1,n+1): 
  for j in range(1,i):
    print("\33[0;34m%10.5f" % L[i][j], end = ' ')
  L[i][i] = 1.0;
  print("\33[m%10.5f" % L[i][i], end = ' ')
  for j in range (i+1, n+1):
    print("\33[m%10.5f" % L[i][j], end = ' ')
  print()   
#:::: 
print(); print("U = "); 
for i in range (1,n+1): 
  for j in range(1,i):
    print("\33[m%10.5f" % U[i][j], end = ' ')
  for j in range (i, n+1):
    print("\33[0;32m%10.5f" % U[i][j], end = '\33[m ')
  print()   
#::::

# 
if teste == 0:
  if abs(A[n][n]) < tolerance:
    teste = 1
if teste < 2: 
  print()
  Det = float(ut)
  for i in range(1,n+1):
    Det = Det*U[i][i]
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
    #::: Para resolver o sistema Ly = Pb
    print() 
    print("Temos LUx = PAx = Pb  e")
    print("informações ao respeito de P estão no vetor\33[1;31m v\33[m.")
    #::: impressao do sistema Ly = Pb
    print(); print("Resolução do sistema Ly = Pb.")
    print("   \33[m b\33[m", end = '') 
    print("   \33[1;31m v\33[m", end ='') 
    for j in range(1,n+1):
      print(end = '          ')
    print("\33[m Pb\33[m") 
    for i in range(1,n+1): 
      print("%7.3f" %b[i], end = '')
      print(" \33[1;31m", v[i], end = ' \33[m ')
      for j in range(1,i):
        print("\33[0;34m %8.5f" % L[i][j], end = '')
      print("\33[m %8.5f" %1.0, end = '') 
      for j in range(i+1,n+1):
        print(end = '         ')
      print("%7.3f" %b[v[i]])
    #::: resolucao do sistema Ly = Pb
    y[1] = b[v[1]]
    for i in range(2, n+1): # i varia de 2 para n
      sum = 0.0
      for j in range(1,i): # j varia de 1 para i-1
        sum = sum + y[j]*L[i][j]
      y[i] = b[v[i]] - sum
    print()
    #
    #::: Para resolver o sistema Ux = y
    #::: Impressão o sistema Ux = y
    print(end = "Resolução do sistema Ux = y.")
    for j in range(1,n+1):
      print(end = '          ')
    print("    \33[m y \33[m")
    for i in range(1,n+1):
      for j in range(1,i):
        print(end = '         ')
      for j in range(i,n+1):
        print("\33[0;32m %8.5f" % U[i][j], end = '')
      print("\33[m %12.6f" % y[i])
    #::: Resolucao do sistema Ux = y    
    x[n] = y[n]/U[n][n]
    for i in range(n-1, 0,-1): # i varia de n-1 para 1
      sum = 0.0
      for j in range(i+1,n+1): # j varia de i+1 para n
        sum = sum + x[j]*U[i][j]
      x[i] = (y[i] - sum)/U[i][i]
  
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