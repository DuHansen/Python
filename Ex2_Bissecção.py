#Um retificador de meia onda a diodo alimenta uma carga indutivaresistiva (f = 1 kHz, L = 100 mH e R = 1 kΩ). Encontre o ‚angulo para
#o qual a corrente Id no diodo se anula. Considere o seguinte modelo
#matem·tico:
#Id = sin(β − φ) + sin(φ)e**(−β/tan(φ))
#tan(φ) = 2πf.L/R  




import math 

def f(x:float,
      o=(math.atan(2*math.pi*abs(0+0.1j))),
      z=(2*math.pi*abs(0+0.1)))->math.degrees:  
    return math.sin(x-o)+math.sin(o)*(math.exp(-x/z))

def bisseccao(x1,  
              x2,  # x2 fim do intervalo
              TOL,  # erro tolerado
              iter=1000):  # número máximo de iterações

    hp = round((x1 + x2)/2 ) # Ponto médio entre os valores x1 e x2
    if f(x1) * f(x2) > 0:
        print("Nenhuma raíz encontrada.")  # nenhuma raíz.
    else:
        c = 0  # variável contador
        ERRO = abs(f(x2) - f(x1))  # diferença entre os valores de y
        while ERRO > TOL or c < iter:  # loop iterativo com critérios de parada
            hp = (x1 + x2) / 2.0
            if f(hp) == 0:
                return [hp, c]
            elif f(x1) * f(hp) < 0:
                x2 = hp
                c += 1  # contagem
            else:
                x1 = hp
            ERRO = abs(f(x2) - f(x1))
        return {"hp": hp*180/math.pi, "iteração": c}  # raíz da função; número de iterações

resp = bisseccao(x1= abs(math.pi), x2= abs(math.pi*2), TOL=0.0001, iter=1000)
print(">>>>>00><00<<<<<")
print(f'raiz aproximada =  {resp["hp"]:.4f}')
print(f'O numero de iteracoes = {resp["iteração"]}')
