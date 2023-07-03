from mpi4py import MPI
import datetime
import numpy as np

def regra_trapezios(x0, xn, n):
    if n == 0:
        print("Divisão por zero")
    elif n < 0:
        print("Intervalo inválido")
    else:
        h = (xn - x0) / n
        x = x0 + h
        soma = 0
        
        for i in range(1, n-1):
            soma += f(x)
            x += h
        
        resultado = h * ((f(x0) + f(xn)) / 2 + soma)
        # print("O resultado da integral da função f ", resultado)

    return resultado

def f(x):
    return 5 * (x**3) + 3 * (x**2) + (4 * x) + 20

x0 = 0
xn = 1000000
n = 10000000
h = (xn - x0) / n

start_time = datetime.datetime.now()

resultado = regra_trapezios(x0, xn, n)

end_time = datetime.datetime.now()
time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() 


# print("Tempo de execução em segundos de relógio: ",wt)
print("Tempo de execucao em segundos: ",execution_time)
print("RESULTADO FINAL=",resultado)
  
  
   
  
