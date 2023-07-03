from mpi4py import MPI

def soma(inicio, fim):
   s=0
   for i in range(inicio, fim+1):
     s=s+i
   
   return s   

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    pedacos = size
    valor = int(input("Digite um valor: "))
    parte = valor // pedacos
    resto = valor % pedacos

    vetinic = [i * parte + min(i, resto) + 1 for i in range(pedacos)]
    vetfim = [(i + 1) * parte + min(i + 1, resto) for i in range(pedacos)]

    for i in range(pedacos):
        vetinic[i] = i * parte + 1
        vetfim[i] = (i + 1) * parte

        if i == pedacos - 1 and vetfim[i] != valor:
            vetfim[i] = valor

    foi = 0

    for i in range(size):
        # Envia vetinic[foi] e vetfim[foi] para o processador i
        comm.send(vetinic[foi], dest=i, tag=1)
        print(i, size)
        comm.send(vetfim[foi], dest=i, tag=2)     
        
        foi += 1

    somapar = 0
    
    while foi <= pedacos - 1:
        # Recebe somaesc de algum processador
        somaesc = comm.recv(source=MPI.ANY_SOURCE)
        print("soma",somaesc)
        id = MPI.Status().Get_source()
        somapar += somaesc

        print(id)
        # Envia vetinic[foi] e vetfim[foi] para o processador id
        comm.send(vetinic[foi], dest=id, tag=1)
        
        comm.send(vetfim[foi], dest=id, tag=2)
        foi += 1
        print('kkkkkkkkkkk')

    for i in range(1, size):
        # Recebe somaesc do processador i
        somaesc = comm.recv(source=i, tag=3)
        somapar += somaesc

    print("Soma final:", somapar)

else:
    inic = comm.recv(source=0, tag=1)
    fim = comm.recv(source=0, tag=2)
    print("inicio", inic)
    print("fim", fim)

    somaesc = soma(inic, fim)
    comm.send(somaesc, dest=0, tag=3)