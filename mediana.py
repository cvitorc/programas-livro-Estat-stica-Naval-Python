#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:38:53 2025

@author: carlosvitor
"""

# Programa para calcular a mediana de uma lista de valores

def calcular_mediana(valores):
    valores_ordenados = sorted(valores)  # Ordena a lista de valores
    n = len(valores_ordenados)
    
    if n == 0:
        return 0  # Evita erro se a lista estiver vazia
    
    meio = n // 2
    
    if n % 2 == 0:
        mediana = (valores_ordenados[meio - 1] + valores_ordenados[meio]) / 2  # Caso par
    else:
        mediana = valores_ordenados[meio]  # Caso ímpar
    
    return mediana

# Exemplo de uso
valores = [8.5, 7.3, 9.0, 6.8, 7.5]  # Lista de notas de alunos
mediana = calcular_mediana(valores)

print(f"Os valores são: {valores}")
print(f"A mediana é: {mediana:.2f}")