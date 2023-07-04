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
        
        for i in range(1, n):
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

valor = 1000000
x0 = 0
xn = 1000000
n = 10000000

pedacos = size - 1  # O número de pedaços é igual ao número de processos - 1
parte = valor // pedacos
resto = valor % pedacos

vetinic = [i * parte + min(i, resto) + 1 for i in range(pedacos)]
vetfim = [(i + 1) * parte + min(i + 1, resto) for i in range(pedacos)]

if rank == 0:
    
    wt = MPI.Wtime()
    start_time = datetime.datetime.now()
    
    pedacos_completos = pedacos
    if resto > 0:
        pedacos_completos -= 1

    vetinic.append(pedacos_completos * parte + min(pedacos_completos, resto) + 1)
    vetfim.append(valor)

    for i in range(size - 1):
        inic = vetinic[i]
        fim = vetfim[i]
        comm.send(inic, dest=i + 1, tag=1)
        comm.send(fim, dest=i + 1, tag=2)

    somapar = 0

    for i in range(pedacos):
        inic = vetinic[i]
        fim = vetfim[i]
        somaesc = regra_trapezios(inic, fim, n)  # Aplicando a função regra_trapezios
        somapar += somaesc
        
    wt = MPI.Wtime() - wt

    end_time = datetime.datetime.now()

    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() 

    print("Tempo de execucao em segundos: ",execution_time)
    print("Resultado final:", somapar)

else:
    inic = comm.recv(source=0, tag=1)
    fim = comm.recv(source=0, tag=2)

    somaesc = regra_trapezios(inic, fim, n)  # Aplicando a função regra_trapezios
    comm.send(somaesc, dest=0, tag=3)
