import matplotlib.pyplot as plt

algoritmos = ['ND', 'BF', 'SD']
tempos = []

for i in range(3):
    tempo = float(input(f"Menor tempo de Execução do Algoritmo {algoritmos[i]}: "))
    tempos.append(tempo)



# Projeta o gráfico de desempenho
fig1, ax1 = plt.subplots()
ax1.bar(algoritmos, tempos)
ax1.set_title("Desempenho dos Algoritmos")
ax1.set_xlabel("Algoritmos")
ax1.set_ylabel("Tempo de Execução (segundos)")



# Criação do gráfico de linha
fig2, ax2 = plt.subplots()
ax2.plot(algoritmos, tempos, marker='o', linestyle='-', color='blue')

# Configurações do gráfico
ax2.set_title("Desempenho dos Algoritmos")
ax2.set_xlabel("Algoritmos")
ax2.set_ylabel("Tempo de Execução (segundos)")


# Exibição do gráfico
plt.show()

