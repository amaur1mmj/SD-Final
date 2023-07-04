import matplotlib.pyplot as plt

def gerar_relatorio(algoritmos, tempos):
    # Configurações do gráfico
    plt.figure(figsize=(10, 6))
    plt.title('Comparação de Melhor Tempo de Execução')
    plt.xlabel('Algoritmos')
    plt.ylabel('Tempo de Execução (segundos)')

    # Plotagem do gráfico de barras
    plt.bar(algoritmos, tempos)

    # Exibição do valor de cada barra no gráfico
    for i, tempo in enumerate(tempos):
        plt.text(i, tempo, str(tempo), ha='center', va='bottom')

    # Exibição do gráfico
    plt.show()
    plt.savefig('img/grafic_melhor_tmp.png')

    # Informações comparativas
    menor_tempo = min(tempos)
    maior_tempo = max(tempos)
    media_tempo = sum(tempos) / len(tempos)

    print('Informações Comparativas:')
    print('Menor tempo de execução:', menor_tempo)
    print('Maior tempo de execução:', maior_tempo)
    print('Tempo médio de execução:', media_tempo)

# Exemplo de utilização
algoritmos = ['Mestre tbm Processa (4p)', 'Butterfly (12p)', 'Balanceamento de Cargas (2p)']
tempos = [0.773706, 0.8242, 2.867871]

gerar_relatorio(algoritmos, tempos)

