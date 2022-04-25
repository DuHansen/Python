import math

def funcao(x):
    return  x*(math.cosh(250/x) - 1)- 50

def metodoBisseccao(a, b):
    if(funcao(a) * funcao(b) >= 0):
        print("A condição f(a) * f(b) < 0 deve ser verdadeira!\n")
        return
    maxIteracoes = 69
    i = 0
    c = a
    erro = 0.00000000001
    while((b - a) >= erro):  
        
        c = (a + b)/2

        if(funcao(c) == 0.0): 
            break

        if(funcao(c) * funcao(a) < 0): 
            b = c
        else:
            a = c

        i = i + 1

    print(">>>>>00><00<<<<<")
    print("    x      = ", "%.8f"%c)
    print("   f(x)    = ", "%.9f"%(funcao(c)))
    print("   Erro    = ", "%.9f" %erro)
    print(" Iterações = ", "%d" %(i-1))

a = 500
b = 1000

metodoBisseccao(a, b)