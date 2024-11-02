#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:31:56 2024

@author: diogo
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

opcao=input('É uma call ou put ?')

if opcao=='call':
    # Definindo as funções de cálculo do payoff da call
    def compra_call(faixa, X, premio_call):
        return np.maximum(faixa - X, 0) - premio_call

    def venda_call(faixa, X, premio_call):
        return premio_call - np.maximum(faixa - X, 0)

    # Parâmetros
    premio_call = float(input('Qual o prêmio da call? '))
    X = float(input('Qual o preço de exercício do ativo? '))
    faixa = np.linspace(0, X * 2, 100)

    # Payoffs
    payoff_compra_call = compra_call(faixa, X, premio_call)
    payoff_venda_call = venda_call(faixa, X, premio_call)

    # Resultado
    resultado_compra_call = payoff_compra_call - premio_call
    resultado_venda_call = payoff_venda_call + premio_call

    # Plotando no gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(faixa, payoff_compra_call, label='Payoff da compra de call', color='b')
    plt.plot(faixa, payoff_venda_call, label='Payoff da Venda de Call', color='r')
    plt.plot(faixa, resultado_compra_call, label='Resultado Call Compra', color='b', linestyle='--')
    plt.plot(faixa, resultado_venda_call, label='Resultado Call Venda', color='r', linestyle='--')

    # Linha de preço de exercício (strike price)
    plt.axvline(X, color='gray', linestyle='--', label='Preco do Strike')

    # Configurações do gráfico
    plt.title('Payoff de Compra e Venda de Call')
    plt.xlabel('Preço do Ativo Subjacente no Vencimento')
    plt.ylabel('Payoff')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    #Tabela de Resultados da Call
    tabela_call = {
        'Opção': ['Compra Call', 'Vende Call'],
        'St>X': [f'St-{X-premio_call}', f"-St-{X+premio_call}"],
        'St<X': [-premio_call, premio_call]
    }

    df = pd.DataFrame(tabela_call)
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.set_title('Tabela de Resultado para a Call', fontsize=15, fontweight='bold')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', bbox=[0, -0.1, 1, 1])
    plt.show()

elif opcao=='put':
    # Definindo as funções de cálculo do payoff da put
    def compra_put(faixa, X, premio_put):
        return np.maximum(X-faixa, 0) - premio_put

    def venda_put(faixa, X, premio_put):
        return premio_put - np.maximum(X-faixa, 0)

    # Parâmetros
    premio_put = float(input('Qual o prêmio da put? '))
    X = float(input('Qual o preço de exercício do ativo? '))
    faixa = np.linspace(0, X * 2, 100)

    # Payoffs
    payoff_compra_put = compra_put(faixa, X, premio_put)
    payoff_venda_put = venda_put(faixa, X, premio_put)

    # Resultado
    resultado_compra_put = payoff_compra_put - premio_put
    resultado_venda_put = payoff_venda_put + premio_put

    # Plotando no gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(faixa, payoff_compra_put, label='Payoff da compra de put', color='b')
    plt.plot(faixa, payoff_venda_put, label='Payoff da Venda de put', color='r')
    plt.plot(faixa, resultado_compra_put, label='Resultado Call put', color='b', linestyle='--')
    plt.plot(faixa, resultado_venda_put, label='Resultado Call put', color='r', linestyle='--')

    # Linha de preço de exercício (strike price)
    plt.axvline(X, color='gray', linestyle='--', label='Preco do Strike')

    # Configurações do gráfico
    plt.title('Payoff de Compra e Venda de Put')
    plt.xlabel('Preço do Ativo Subjacente no Vencimento')
    plt.ylabel('Payoff')
    plt.legend()
    plt.grid(True)
    plt.show()

    #Tabela de Resultados da Put
    tabela_put = {
        'Opção': ['Compra Put', 'Vende Put'],
        'St>X': [-premio_put, premio_put],
        'St<X': [f"-St+{X-premio_put}", f'-St+{premio_put-X}']
    }

    df = pd.DataFrame(tabela_put)
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.set_title('Tabela de Resultado para a Put', fontsize=15, fontweight='bold')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    plt.show()
  
    df = pd.DataFrame(tabela_put)
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.set_title('Tabela de Resultado para a Put', fontsize=15, fontweight='bold')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', bbox=[0, -0.1, 1, 1])
    plt.show()

else:print('A escolha deve ser call ou put')
    
    