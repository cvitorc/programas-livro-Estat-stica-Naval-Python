#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:39:40 2025


Explicação do Código:
Função calcular_media: Recebe uma lista de valores e calcula a média.
Verificação de lista vazia: Caso a lista esteja vazia, o programa retorna zero para evitar erro de divisão por zero.
Uso de sum() e len(): A função sum soma todos os valores da lista, e len conta quantos elementos existem.
Formatação do resultado: A média é exibida com duas casas decimais (:.2f).

@author: carlosvitor
"""

# Programa para calcular a média aritmética de uma lista de valores

def calcular_media(valores):
    if len(valores) == 0:
        return 0  # Evita divisão por zero
    
    soma = sum(valores)  # Soma todos os elementos da lista
    media = soma / len(valores)  # Divide a soma pelo número de elementos
    
    return media

# Exemplo de uso
valores = [8.5, 7.3, 9.0, 6.8, 7.5]  # Lista de notas de alunos
media = calcular_media(valores)

print(f"Os valores são: {valores}")
print(f"A média aritmética é: {media:.2f}")



