import numpy as np 


def LU_Decomposition_method(A, b):  # cria-se a função do método
    m = len(A)
    y = np.zeros(m)
    x = np.zeros(m)
    U = A
    L = np.zeros([m, m])
    for k in range(0, m):
        for r in range(0, m):
            if (k == r):
                L[k, r] = 1
            if (k < r):
                factor = (A[r, k]/A[k, k])
                L[r, k] = factor
                for c in range(0, m):
                    U[r, c] = A[r, c] - (factor * A[k, c])
    A = np.zeros([m, m])
    for r in range(0, m):
        for c in range(0, m):
            for k in range(0, m):
                A[r, c] += (L[r, k] * U[k, c])
    print('A')
    print(A)
    print('L')
    print(L)
    print()
    print('U')
    print(U)
    # RESOLUÇÃO DAS EQUAÇÕES MATRICIAIS
    ###################################
    y:float = np.linalg.solve(L, b)
    x:float = np.linalg.solve(U, y)
    ###################################
    f = 'SOLUÇÃO DO SISTEMA'
    print('-'*(len(f)+32))
    print(f'{f:^50}')
    print('-'*(len(f)+32))
    print('x =')
    print(x)
    print('Onde: ')
    for c in range(0, len(x)):
        print(f'\t x[{c}] = {x[c]} \n')



# Uso do método
A = np.array([[6,-3,-3,0,0],
     [-3,6,0,-3,0],
     [-3,0,6,-1,-2],
     [0,-3,-1,5,0],
     [0,0,-2,0,3]],float)
b = np.transpose([0,6,0,2,-3])
LU_Decomposition_method(A, b)



