#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:40:00 2025

@author: carlosvitor
"""

# Programa para calcular a variância de uma lista de valores

def calcular_media(valores):
    if len(valores) == 0:
        return 0  # Evita divisão por zero
    
    soma = sum(valores)  # Soma todos os elementos da lista
    media = soma / len(valores)  # Divide a soma pelo número de elementos
    
    return media

def calcular_variancia(valores):
    if len(valores) == 0:
        return 0  # Lista vazia
    
    media = calcular_media(valores)  # Usa a função de média já implementada
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    
    return variancia

# Exemplo de uso
valores = [8.5, 7.3, 9.0, 6.8, 7.5]  # Lista de notas de alunos
variancia = calcular_variancia(valores)

print(f"Os valores são: {valores}")
print(f"A variância é: {variancia:.2f}")