#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:56:16 2024

@author: diogo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('/Users/diogo/Downloads/APS-FIN3.xlsx',sheet_name= 'Câmbio ')
cambio = df['EURO/DOLAR CPA'].dropna()

log_retorno = np.log(cambio / cambio.shift(1)).dropna()

sim = 1000000
faixa = 252  # 252 dias
np.random.seed(300) 

retorno_simulado = np.random.choice(log_retorno, size=(sim, faixa), replace=True)
exp_retorno_simulado= np.exp(retorno_simulado.sum(axis=1))

expo_inicial = 29670652173  #bilhões de Dólares
expo_simulado = expo_inicial * exp_retorno_simulado

perdas = expo_inicial - expo_simulado

alfa = 0.95
var_95 = np.percentile(perdas, (1 - alfa) * 100)
var_por_cento=-var_95/expo_inicial * 100

print(f'Value at Risk (VaR) com 95% de confiança: €{var_95:,.2f}')
print(f'Value at Risk (VaR) com 95% de confiança (%): {var_por_cento:,.2f}')

# Visualização do histograma das perdas
plt.hist(perdas, bins=50, color='darkblue', edgecolor='black')
plt.axvline(x=var_95, color='red', label=f'var_95: EUR {abs(var_95):,.2f}')
plt.title('Distribuição Simulada')
plt.xlabel('Perda Máxima em US$')
plt.ylabel('Frequência')
plt.legend()
plt.show()

