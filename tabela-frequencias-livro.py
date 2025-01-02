#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 21:43:58 2025

@author: carlosvitor
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dados das velocidades de 50 embarcações (em nós)
velocidades = [12, 14, 13, 17, 18, 14, 15, 16, 20, 13, 11, 19, 15, 14, 18, 17, 21, 16, 14, 15,
               18, 16, 14, 17, 20, 22, 13, 15, 12, 14, 13, 11, 15, 16, 17, 20, 19, 14, 15, 14,
               13, 15, 18, 16, 19, 20, 15, 13, 17, 16]

# A construção da tabela de frequência é um processo que organiza e resume os dados de forma estruturada.
# Primeiramente, determina-se o número de classes (intervalos) usando a raiz quadrada do total de observações,
# o que proporciona uma divisão equilibrada dos dados. Em seguida, cria-se os intervalos de classe com a função
# np.linspace, garantindo que os dados sejam distribuídos uniformemente. Para cada intervalo, calcula-se a
# frequência absoluta (número de dados que caem dentro de cada faixa). A partir daí, obtém-se a frequência
# relativa (proporção em relação ao total de dados) e a frequência acumulada (soma progressiva das frequências).
# O ponto médio de cada intervalo é calculado para representar graficamente as classes de forma precisa.

# O cálculo do tamanho do intervalo de classe é feito dividindo a diferença entre o valor máximo e o valor mínimo dos dados
# pelo número de classes. Isso resulta em intervalos de tamanho uniforme, garantindo uma distribuição equilibrada dos dados
# ao longo do histograma. Esse método facilita a visualização de tendências e padrões. A função np.linspace é utilizada
# para criar os intervalos de classe de forma automática, garantindo que o espaço entre cada limite seja constante.

# Passo 1: Determinar número de classes
# O número de classes é calculado usando a raiz quadrada do total de elementos
num_classes = int(np.sqrt(len(velocidades)))  # sqrt(50) ≈ 7

# Passo 2: Determinar intervalo de classe (faixas de valores)
# np.linspace cria uma sequência de valores igualmente espaçados de min(velocidades) até max(velocidades)
# O +1 garante que tenhamos um ponto a mais para formar 7 intervalos
intervalo_classes = np.linspace(min(velocidades), max(velocidades), num_classes + 1)

# Passo 3: Calcular frequência absoluta
# np.histogram retorna a contagem de elementos (frequência absoluta) em cada intervalo de classe definido
frequencia_absoluta, bins = np.histogram(velocidades, bins=intervalo_classes)

# Passo 4: Calcular frequência relativa
# A frequência relativa é obtida dividindo a frequência absoluta pelo total de elementos
frequencia_relativa = frequencia_absoluta / len(velocidades)

# Passo 5: Calcular frequência acumulada
# np.cumsum retorna a soma cumulativa dos valores, criando a frequência acumulada
frequencia_acumulada = np.cumsum(frequencia_absoluta)

# Passo 6: Calcular ponto médio de cada intervalo de classe
# O ponto médio é a média dos limites superior e inferior de cada intervalo
ponto_medio = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]

# Exibir tabela de frequências em formato de DataFrame do pandas
# A tabela mostra o intervalo de classe, ponto médio, frequência absoluta, relativa e acumulada
tabela = pd.DataFrame({
    'Intervalo de Classe': [f'{int(bins[i])}-{int(bins[i+1])}' for i in range(len(bins)-1)],
    'Ponto Médio': ponto_medio,
    'Frequência Absoluta': frequencia_absoluta,
    'Frequência Relativa': frequencia_relativa,
    'Frequência Acumulada': frequencia_acumulada
})

# Imprime a tabela de frequências no console
print(tabela)

# Plotar o histograma
plt.figure(figsize=(10, 6))  # Define o tamanho do gráfico
plt.hist(velocidades, bins=intervalo_classes, edgecolor='black', rwidth=0.9)  # Plota o histograma
plt.title('Histograma das Velocidades das Embarcações')  # Título do gráfico
plt.xlabel('Velocidade (nós)')  # Rótulo do eixo X
plt.ylabel('Frequência')  # Rótulo do eixo Y
plt.xticks(np.arange(min(velocidades), max(velocidades) + 1, 1))  # Define as marcas do eixo X
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adiciona uma grade pontilhada no eixo Y

# Marcar pontos médios no histograma e desenhar linhas verticais até o eixo X
for i in range(len(ponto_medio)):
    # Exibe o valor do ponto médio acima de cada barra
    plt.text(ponto_medio[i], frequencia_absoluta[i] + 0.5, str(round(ponto_medio[i], 1)), ha='center')
    # Desenha linhas verticais no ponto médio descendo até o eixo X
    plt.vlines(ponto_medio[i], 0, frequencia_absoluta[i], colors='red', linestyles='dashed')


# Salvando o gráfico como imagem
plt.savefig("grafico-histograma.png", format="png", dpi=300)

# Exibe o gráfico
plt.show()


