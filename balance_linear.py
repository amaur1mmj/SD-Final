from mpi4py import MPI

def soma(inicio, fim):
   s = 0
   for i in range(inicio, fim + 1):
       s += i
   return s   

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

valor = 5

pedacos = size - 1  # O número de pedaços é igual ao número de processos - 1
parte = valor // pedacos
resto = valor % pedacos

vetinic = [i * parte + min(i, resto) + 1 for i in range(pedacos)]
vetfim = [(i + 1) * parte + min(i + 1, resto) for i in range(pedacos)]

if rank == 0:
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
        somaesc = comm.recv(source=i + 1, tag=3)
        somapar += somaesc

    print("Soma final:", somapar)

else:
    inic = comm.recv(source=0, tag=1)
    fim = comm.recv(source=0, tag=2)

    somaesc = soma(inic, fim)
    comm.send(somaesc, dest=0, tag=3)
