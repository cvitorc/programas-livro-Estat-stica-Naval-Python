#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:41:06 2025

@author: carlosvitor
"""

# Programa para calcular o desvio padrão de uma lista de valores
import math

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


def calcular_desvio_padrao(valores):
    if len(valores) == 0:
        return 0  # Lista vazia
    
    variancia = calcular_variancia(valores)  # Usa a função de variância já implementada
    desvio_padrao = math.sqrt(variancia)  # Calcula a raiz quadrada da variância
    
    return desvio_padrao

# Exemplo de uso
valores = [8.5, 7.3, 9.0, 6.8, 7.5]  # Lista de notas de alunos
desvio_padrao = calcular_desvio_padrao(valores)

print(f"Os valores são: {valores}")
print(f"O desvio padrão é: {desvio_padrao:.2f}")