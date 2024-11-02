import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy_financial as npf


"DINÂMICA DE SISTEMAS (parte 1) - Tendência de equilíbrio entre preço e Demanda TOTAL x Oferta"

# gamma: coeficiente de variação do preço pela diferença entre demanda e oferta
gamma = 0.5

# preço inicial
P0 = 1150 # em U$D

# vetor tempo
t = np.arange(0, 5 + 1/12, 1/12)

# função com equação diferencial
def EqDif(Y, t):
    P = Y[0]
    Qd = 624.256 - 0.32544*P
    Qs = -176.248 + 0.23152*P
    dPdt = gamma*(Qd - Qs)
    return(dPdt)

# resolução da equação diferencial
Y = odeint(EqDif, P0, t)

preço_esperado = np.zeros(len(Y))
for i in range (0, len(Y)):
    preço_esperado[i] = Y[i][0]

'''
# gráfico preço x tempo
plt.plot(t, preço_esperado)
plt.title('Variação do Preço da embalagem orgânica')
plt.xlabel('Tempo (anos)')
plt.ylabel('Preço (U$D/Tonelada)')
'''


"DINÂMICA DE SISTEMAS (parte 2) - Tendência de troca da Fibra Longa pelo Eukaliner"

# theta:
θ = 0.04

# proporção inicial de Eukaliner (qtde eukaliner/(qtde eukaliner + qtde fibra longa))
Proporção_inicial_Eukaliner = 0 # em porcentagem

# vetor tempo
t = t # mesmo vetor de antes

# função com equação diferencial
def EqDif(W, t):
    dProporçãoEdt = 2*θ*t*100
    return(dProporçãoEdt)

# resolução da equação diferencial
W = odeint(EqDif, Proporção_inicial_Eukaliner, t)

proporção_eukaliner = np.zeros(len(W))
for i in range (0, len(W)):
    proporção_eukaliner[i] = W[i][0]/100

'''
# gráfico preço x tempo
plt.plot(t, W)
plt.title('Variação da proporção de Eukaliner')
plt.xlabel('Tempo (anos)')
plt.ylabel('Quantidade de Eukaliner (%)')
'''

def VPLsim(tma):
    "ESTOQUE E SIMULAÇÃO"
    # A demanda de cada mês vai variar em torno da função Qd = 624.256 - 0.32544*P considerando P ~ N(µ, 82.7130267670679), sendo µ a projeção do preço na parte 1 de DINÂMICA DE SISTEMAS, e 82,7130267670679 o desvio padrão do preço calculado a partir dos dados históricos da cotação da fibra longa nos meses de 2022.
    # A cotação do dólar vai variar a cada mês de acordo com uma distribuição N(5.29, 0,227410757912253), sendo 5.29 a última cotação do ano de 2022 e 0,227410757912253 o desvio padrão calculado a partir dos dados históricos da cotação do dólar nos meses de 2022.
    
    # tamanho do lote
    lote = 200 # em milhares de toneladas
    
    # custo unitário de armazenagem 
    custo_unit_armazenagem = 10**6 # em R$/tonelada
    
    # custo com aluguel de armazéns
    custo_aluguel = 5*(10**5) # em R$/armazém
    
    # custo de fabricação de um lote completo para cada material
    custo_fab_eukaliner = 1.5*(10**7)
    custo_fab_fibra_longa = 3*(10**7)
    
    # projeção da demanda total, cotação do dólar, estoque e lotes fabricados
    oferta_total = np.zeros(61)
    demanda_total = np.zeros(61)
    vendas = np.zeros(61)
    cotação_dólar = np.zeros(61)
    estoque_mensal = np.zeros(61)
    preço = np.zeros(61)
    estoque_mensal[0] = lote
    lotes_fabricados = np.zeros(61)
    lotes_fabricados[0] = 1
    armazens_extras = np.zeros(61)
    custo_fab_lote = np.zeros(61)
    custo_fab_lote[0] = custo_fab_eukaliner*proporção_eukaliner[0] + custo_fab_fibra_longa*(1 - proporção_eukaliner[0])
    for i in range (1, 61):
        preço[i] = np.random.normal(preço_esperado[i], 82.7130267670679)
        oferta_total[i] = -176.248 + 0.23152*preço[i]
        demanda_total[i] = 624.256 - 0.32544*preço[i]
        cotação_dólar[i] = np.random.normal(5.29, 0.227410757912253)
        
        if oferta_total[i] <= demanda_total[i]:
            estoque_mensal[i] = estoque_mensal[i - 1] - oferta_total[i]
            vendas[i] = oferta_total[i]
        
        elif oferta_total[i] > demanda_total[i]:
            estoque_mensal[i] = estoque_mensal[i - 1] - demanda_total[i]
            vendas[i] = demanda_total[i]
            
        if estoque_mensal[i] <= 0:
            estoque_mensal[i] = estoque_mensal[i] + lote
            lotes_fabricados[i] += 1
            custo_fab_lote[i] = custo_fab_eukaliner*proporção_eukaliner[i] + custo_fab_fibra_longa*(1 - proporção_eukaliner[i])
            
        if estoque_mensal[i] <= 0: # camada de segurança, caso a demanda de algum mês seja muito alta
            estoque_mensal[i] = estoque_mensal[i] + lote
            lotes_fabricados[i] += 1
            custo_fab_lote[i] = custo_fab_eukaliner*proporção_eukaliner[i] + custo_fab_fibra_longa*(1 - proporção_eukaliner[i])
            
        if estoque_mensal[i] >= 200:
            armazens_extras[i] = armazens_extras[i] + 1
    
    
    "FINANÇAS 1"
    
    # Fluxo de caixa com a venda (valor residual)
    taxa_ir =  0.299078814252499 
    investimento = 1.2*(10**10)
    depreciação_anual = investimento/8
    valor_residual = 2.5*(10**9)
    valor_contábil = investimento - 5*depreciação_anual
    FCx_venda = (valor_residual - valor_contábil)*(1 - taxa_ir)
    
    # DRE
    receita = np.zeros(6)
    custo_total_anual = np.zeros(6)
    depreciação = depreciação_anual
    lajir = np.zeros(6)
    ir = np.zeros(6)
    nopat = np.zeros(6)
    
    for i in range (1, 6):
        custo_unit_anual = 0
        custo_fab_anual = 0
        custo_aluguel_anual = 0
        
        for j in range (1, 13):
            custo_unit_anual = custo_unit_anual + custo_unit_armazenagem*estoque_mensal[12*(i - 1) + j]
            custo_fab_anual = custo_fab_anual + custo_fab_lote[12*(i - 1) + j]
            custo_aluguel_anual = custo_aluguel_anual + custo_aluguel*armazens_extras[12*(i - 1) + j]
            receita[i] = receita[i] + 1000*(preço[12*(i - 1) + j]*vendas[12*(i - 1) + j])*cotação_dólar[12*(i - 1) + j]
    
        custo_total_anual[i] = custo_unit_anual + custo_fab_anual + custo_aluguel_anual + 12*custo_aluguel
        lajir[i] = receita[i] - custo_total_anual[i] - depreciação
        ir[i] = lajir[i]*taxa_ir
        nopat[i] = lajir[i] - ir[i]
        
    # Fluxo de caixa do projeto
    fluxo_operacional = np.zeros(6)
    capex = np.zeros(6)
    fluxo_projeto = np.zeros(6)
    
    capex[0] = -investimento
    capex[-1] = FCx_venda
    fluxo_projeto[0] = fluxo_operacional[0] + capex[0]
    
    for i in range (1,6):
        fluxo_operacional[i] = nopat[i] + depreciação
        fluxo_projeto[i] = fluxo_operacional[i] + capex[i]
    
    # VPL e TIR
    VPL = npf.npv(tma, fluxo_projeto)
    TIR = npf.irr(fluxo_projeto)
    return (VPL, TIR)

"SIMULAÇÃO DE MONTE CARLO"

n = 1000
tma = 0.2
VPL = np.zeros(n)
TIR = np.zeros(n)

for i in range (0, n):
    VPL[i] = VPLsim(tma)[0]
    TIR[i] = VPLsim(tma)[1]


print(np.mean(VPL))
print(np.mean(TIR))

plt.hist(VPL, bins = 10)
plt.title('VPLs simulados')
plt.xlabel('VPL')
plt.ylabel('Frequência')







