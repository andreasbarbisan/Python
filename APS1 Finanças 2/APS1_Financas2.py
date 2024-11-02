import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize
import matplotlib.ticker as mtick

# caminho do arquivo com os dados
caminho_arquivo = r"C:\Users\andreas\Downloads\Base de Dados Final.xlsx"

# carregando os dados
retornos = pd.read_excel(caminho_arquivo, sheet_name = 'Ativos com risco', header = 0, index_col = 0)

# cálculo da média e matriz de covariâncias
media_retornos = retornos.mean()
matriz_cov = retornos.cov()

# lista com os nomes dos ativos
lista_acoes = retornos.columns.tolist()

n = 1000000 # número de simulações

# definindo vetores para armazenar os resultados das simulações
vetor_retornos_esperados = np.zeros(n)
vetor_volatilidades_esperadas = np.zeros(n)
vetor_sharpe = np.zeros(n)
tabela_pesos = np.zeros((n, len(lista_acoes)))

# definindo o risk free
risk_free = 1.01085762179045/100

# definindo as aversões ao risco
baixa_aversao = 4  # Baixa aversão ao risco (amante ao risco)
media_aversao = 6.5  # Média aversão ao risco
alta_aversao = 12   # Alta aversão ao risco (avesso ao risco)

# simulações
for i in range(n):
    
    # gerando pesos aleatórios e normalizando
    pesos = np.random.random(len(lista_acoes))
    pesos = pesos/np.sum(pesos)
    tabela_pesos[i, :] = pesos
    
    # retorno esperado e volatilidade esperada
    vetor_retornos_esperados[i] = np.sum(media_retornos * pesos)
    vetor_volatilidades_esperadas[i] = np.sqrt(np.dot(pesos.T, np.dot(matriz_cov, pesos)))
    
    # sharpe
    vetor_sharpe[i] = (vetor_retornos_esperados[i] - risk_free)/vetor_volatilidades_esperadas[i]

# sharpe e pesos ótimos
posicao_sharpe_maximo = vetor_sharpe.argmax()
pesos_otimos = tabela_pesos[posicao_sharpe_maximo, :]
pesos_otimos = [str((peso * 100).round(2)) + "%" for peso in pesos_otimos]

# imprimindo os pesos ótimos de cada ativo
for i, acao in enumerate(lista_acoes):
    print(f"Peso {acao}: {pesos_otimos[i]}")

# fronteira de mínima variância
eixo_y_fronteira_eficiente = np.linspace(vetor_retornos_esperados.min(), vetor_retornos_esperados.max(), 100)

def pegando_retorno(peso_teste):
    peso_teste = np.array(peso_teste)
    retorno = np.sum(media_retornos *peso_teste)
    return retorno

def checando_soma_pesos(peso_teste):
    return np.sum(peso_teste) - 1

# cálculo da carteira de risco com mínima variância
def pegando_vol(peso_teste):
    peso_teste = np.array(peso_teste)
    vol = np.sqrt(np.dot(peso_teste.T, np.dot(matriz_cov, peso_teste)))
    return vol

peso_inicial = [1/len(lista_acoes)] * len(lista_acoes)
limites = tuple([(0, 1) for ativo in lista_acoes])
eixo_x_fronteira_eficiente = []

for retorno_possivel in eixo_y_fronteira_eficiente:
    
    restricoes = ({'type': 'eq', 'fun': checando_soma_pesos}, {'type': 'eq', 'fun': lambda w: pegando_retorno(w) - retorno_possivel})
    
    result = minimize(pegando_vol, peso_inicial, method = 'SLSQP', bounds = limites, constraints = restricoes)
    
    eixo_x_fronteira_eficiente.append(result['fun'])
   
# cálculo das das alocações ótimas de cada perfil na carteira de risco ótima
w_otimo_baixo_risco = (vetor_retornos_esperados[posicao_sharpe_maximo] - risk_free)/(baixa_aversao*(vetor_volatilidades_esperadas[posicao_sharpe_maximo]**2))
w_otimo_medio_risco = (vetor_retornos_esperados[posicao_sharpe_maximo] - risk_free)/(media_aversao*(vetor_volatilidades_esperadas[posicao_sharpe_maximo]**2))
w_otimo_alto_risco = (vetor_retornos_esperados[posicao_sharpe_maximo] - risk_free)/(alta_aversao*(vetor_volatilidades_esperadas[posicao_sharpe_maximo]**2))

# cálculo dos retornos de cada perfil
retorno_baixo = vetor_retornos_esperados[posicao_sharpe_maximo]*w_otimo_baixo_risco + (1 - w_otimo_baixo_risco)*risk_free
retorno_medio = vetor_retornos_esperados[posicao_sharpe_maximo]*w_otimo_medio_risco + (1 - w_otimo_medio_risco)*risk_free
retorno_alto = vetor_retornos_esperados[posicao_sharpe_maximo]*w_otimo_alto_risco + (1 - w_otimo_alto_risco)*risk_free

# cálculo das volatilidades de cada perfil
volatilidade_baixo = vetor_volatilidades_esperadas[posicao_sharpe_maximo]*w_otimo_baixo_risco
volatilidade_medio = vetor_volatilidades_esperadas[posicao_sharpe_maximo]*w_otimo_medio_risco
volatilidade_alto = vetor_volatilidades_esperadas[posicao_sharpe_maximo]*w_otimo_alto_risco

# Criação do gráfico
fig, ax = plt.subplots()

# Plotando os pontos das simulações com cores baseadas na razão de Sharpe
scatter = ax.scatter(vetor_volatilidades_esperadas, vetor_retornos_esperados, c = vetor_sharpe, cmap = 'inferno')
plt.colorbar(scatter, label = 'Razão de Sharpe')

# Adicionando a fronteira de mínima variância ao gráfico
ax.plot(eixo_x_fronteira_eficiente, eixo_y_fronteira_eficiente, linewidth = 3.5, label = 'Fronteira de Mínima Variância')

# Formatadores para os eixos em formato percentual
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1, 0))
ax.xaxis.set_major_formatter(mtick.PercentFormatter(1, 0))

# Cálculo dos valores para a LAC ótima
vol_otima = vetor_volatilidades_esperadas[posicao_sharpe_maximo]
retorno_otimo = vetor_retornos_esperados[posicao_sharpe_maximo]
alc_x = [0, vol_otima * 2]
alc_y = [risk_free, risk_free + (retorno_otimo - risk_free) / vol_otima * vol_otima * 2]

# Plotando a LAC ótima
ax.plot(alc_x, alc_y, color = 'grey', linestyle = '--', linewidth = 3, label = 'LAC Ótima')

# Encontrar os pesos que minimizam a volatilidade
pesos_min_var = minimize(pegando_vol, peso_inicial, method = 'SLSQP', bounds = limites, constraints = {'type': 'eq', 'fun': checando_soma_pesos})

# Calculando o retorno esperado e a volatilidade para a carteira de mínima variância
retorno_min_var = pegando_retorno(pesos_min_var.x)
vol_min_var = pegando_vol(pesos_min_var.x)

# Filtrar para manter apenas os pontos da fronteira eficiente
indices_fronteira_eficiente = eixo_y_fronteira_eficiente >= vetor_retornos_esperados[vetor_volatilidades_esperadas.argmin()]
eixo_x_fronteira_eficiente_filtrado = np.array(eixo_x_fronteira_eficiente)[indices_fronteira_eficiente]
eixo_y_fronteira_eficiente_filtrado = eixo_y_fronteira_eficiente[indices_fronteira_eficiente]

# Adicionando a fronteira eficiente filtrada ao gráfico
ax.plot(eixo_x_fronteira_eficiente_filtrado, eixo_y_fronteira_eficiente_filtrado, linewidth = 3, label = 'Fronteira Eficiente', color = 'red', linestyle = '--')

# Ajustes finais e configuração dos rótulos e legenda
ax.set_xlabel("Volatilidade esperada")
ax.set_ylabel("Retorno esperado")
ax.legend()

# Ajustando os limites dos eixos
ax.set_xlim([0, 0.10])
ax.set_ylim([0, 0.04])

ax.scatter(volatilidade_baixo, retorno_baixo, color = "blue", s = 70, edgecolors = "black", label = 'Amante ao Risco', zorder = 5)
ax.scatter(volatilidade_medio, retorno_medio, color = "green", s = 70, edgecolors = "black", label = 'Média Aversão ao Risco', zorder = 5)
ax.scatter(volatilidade_alto, retorno_alto, color = "yellow", s = 70, edgecolors = "black", label = 'Alta Aversão ao Risco', zorder = 5)

# Plotando o ponto da carteira de risco ótima
ax.scatter(vetor_volatilidades_esperadas[posicao_sharpe_maximo], vetor_retornos_esperados[posicao_sharpe_maximo], color = "red", edgecolors = 'black', label = 'Carteira de Risco Ótima (P*)', s = 70)

# Plotando o ponto da carteira de mínima variância
ax.scatter(vol_min_var, retorno_min_var, color = 'orange', s = 70, edgecolors = 'black', label = 'Carteira de Mínima Variância')

ax.legend()

# Exibição do gráfico
plt.show()

print(f"Sharpe: {max(vetor_sharpe)}")
print(f"Risco p*: {vetor_volatilidades_esperadas[posicao_sharpe_maximo]}")
print(f"Retorno p*: {vetor_retornos_esperados[posicao_sharpe_maximo]}")
print("")
print(f"Risco Wilson (A = {alta_aversao}): {volatilidade_alto}")
print(f"Retorno Wilson (A = {alta_aversao}): {retorno_alto}")
print(f"Peso Wilson (A = {alta_aversao}): {w_otimo_alto_risco}")
print("")
print(f"Risco Fernando (A = {media_aversao}): {volatilidade_medio}")
print(f"Retorno Fernando (A = {media_aversao}): {retorno_medio}")
print(f"Peso Fernando (A = {media_aversao}): {w_otimo_medio_risco}")
print("")
print(f"Risco Priscila (A = {baixa_aversao}): {volatilidade_baixo}")
print(f"Retorno Priscila (A = {baixa_aversao}): {retorno_baixo}")
print(f"Peso Priscila (A = {baixa_aversao}): {w_otimo_baixo_risco}")
print("")
print(matriz_cov)
