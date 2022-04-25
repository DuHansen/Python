import math
from math import e, pi

def f(x):
  return x*(math.cosh(250/x) - 1)- 50

  def bisseccao (x1,
                 x2,
                 tol,
                 iter= 30):
    
    hp = (x1 + x2)/2
    if f(x1)* f(x2)> 0:
      print("Nenhuma raiz encontrada.")
    else:
        c = 0
        ERRO = abs(f(x2)-f(x1))
    
        while ERRO >tol or c<iter:

          hp = (x1 + x2)/2.0
          if f(hp) == 0:
              return [hp, c]
          elif f(x1) * f(hp)< 0:
              x2 = hp
              c +=1
          else:
                x1 = hp
                ERRO = abs(f(x2) - f(x1))
                return {"hp": hp, "itera": c}

      
          print (f'raiz{resp["hp"]: . 4f}')  
          print (f'iterações {resp["itera"]}') 