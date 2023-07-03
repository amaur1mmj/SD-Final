from mpi4py import MPI
import datetime

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


wt = MPI.Wtime()
start_time = datetime.datetime.now()

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
x0 = 0
xn = 1000000
n = 10000000
h = (xn - x0) / n
    
    
local_n = n // size
local_x0 = x0 + rank * local_n * h
local_xn = local_n * h * (rank + 1)
if(rank == size-1):
    fim=xn


resultado = regra_trapezios(local_x0, local_xn, local_n)

tamanho = size

while rank < tamanho and tamanho > 1:
    metade = tamanho // 2
    soma = resultado
    if rank  >= metade:
        comm.send(soma, dest=rank - metade)
        
    else:
        soma_recebida = comm.recv(source=rank + metade)
        resultado += soma_recebida

    tamanho = metade
        
    


if rank == 0:
    wt = MPI.Wtime() - wt

    end_time = datetime.datetime.now()

    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() 
    # print("Tempo de execução em segundos de relógio: ",wt)
    # print("Tempo de execução02 em segundos de relógio: ",execution_time)
    print("Tempo de execucao em segundos: ",execution_time)
    print("O resultado final é:", resultado)
