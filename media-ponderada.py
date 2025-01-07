#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:20:36 2025

@author: carlosvitor
"""

# Programa para calcular a média ponderada de uma lista de valores

def calcular_media_ponderada(valores, pesos):
    if len(valores) == 0 or len(valores) != len(pesos):
        return 0  # Evita divisão por zero ou lista inválida
    
    soma_ponderada = sum(v * p for v, p in zip(valores, pesos))  # Soma dos produtos valor * peso
    soma_pesos = sum(pesos)  # Soma total dos pesos
    
    media_ponderada = soma_ponderada / soma_pesos  # Divide a soma ponderada pela soma dos pesos
    
    return media_ponderada

# Exemplo de uso
valores = [8.5, 7.3, 9.0, 6.8, 7.5]  # Lista de notas de alunos
pesos = [2, 3, 4, 1, 2]  # Pesos correspondentes
media_ponderada = calcular_media_ponderada(valores, pesos)

print(f"Os valores são: {valores}")
print(f"Os pesos são: {pesos}")
print(f"A média ponderada é: {media_ponderada:.2f}")