#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:39:33 2025

@author: carlosvitor
"""

from collections import Counter

# Programa para calcular a moda de uma lista de valores

def calcular_moda(valores):
    if len(valores) == 0:
        return None  # Lista vazia
    
    contagem = Counter(valores)
    max_frequencia = max(contagem.values())
    moda = [k for k, v in contagem.items() if v == max_frequencia]
    
    return moda

# Exemplo de uso
valores = [8.5, 7.3, 9.0, 6.8, 7.5, 7.3, 8.5]  # Lista de notas de alunos
moda = calcular_moda(valores)

print(f"Os valores são: {valores}")
print(f"A moda é: {moda}")