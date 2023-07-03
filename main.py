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

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()



x0 = 0
xn = 1000000
n = 10000000
h = (xn - x0) / n


if rank == 0:
    

    wt = MPI.Wtime()
    start_time = datetime.datetime.now()

    local_n = n // size
    local_x0 = x0 + rank * local_n * h
    local_xn = local_n * h * (rank + 1)
    if(rank == size-1):
        fim=xn


    resultado = regra_trapezios(local_x0, local_xn, local_n)

    resultado=comm.reduce(resultado,op=MPI.SUM, root=0) #faz o reduce de soma de todos os processos com raiz(root) no mestre(0) com operacao de soma (MPI.SUM)
        
    wt = MPI.Wtime() - wt

    end_time = datetime.datetime.now()

    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() 

    

    print("Tempo de execucao em segundos: ",execution_time)
    print("RESULTADO FINAL=",resultado)
  
else:

    local_n = n // size
    local_x0 = x0 + rank * local_n * h + 1
    local_xn = local_n * h * (rank + 1)
    if(rank == size-1):
        fim=xn


    resultado = regra_trapezios(local_x0, local_xn, local_n)

    resultado=comm.reduce(resultado,op=MPI.SUM, root=0) #faz o reduce de soma de todos os processos com raiz(root) no mestre(0) com operacao de soma (MPI.SUM)