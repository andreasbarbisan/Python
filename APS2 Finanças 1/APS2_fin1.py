import numpy as np
import matplotlib.pyplot as plt
import numpy_financial as npf

# Parâmetros da simulação
custoEUKALINER = 650
quantidadeEUKALINER = 350000
depre = 437500000

# Simulação para cotação do dólar e preço do Eukaliner
dolar = np.random.normal(5.29, 0.227410758, 100000)
preçoEUKALINER = np.random.normal(1437.28, 82.71302677, 100000)

# Cálculo da receita para os anos do projeto
receita = [quantidadeEUKALINER * preçoEUKALINER * dolar for _ in range(5)]
cmv = [quantidadeEUKALINER * custoEUKALINER * dolar for _ in range(5)]

# Cálculo do LAJIR, NOPAT e FCO
lajir = [receita[i] - cmv[i] - depre for i in range(5)]
nopat = [lajir[i] - (lajir[i] * 0.2990788) for i in range(5)]
FCO = [nopat[i] + depre for i in range(5)]

# Cálculo do Fluxo de Caixa para cada ano
FCx = np.zeros((6, 100000))
FCx[0] = -3500000000
for i in range(5):
    FCx[i + 1] = FCO[i]
FCx[5] += 832343908.08  # Ajuste para o último ano, incluindo valor de venda

# Cálculo do VPL
TMA = 0.2
VPL = npf.npv(TMA, FCx)

# Visualização dos resultados
plt.hist(VPL, bins=50, color='blue', alpha=0.7)
plt.axvline(x=0, color='purple', linestyle='--', label='VPL = 0')
plt.title("Distribuição do VPL do Projeto de Investimento")
plt.xlabel("VPL")
plt.ylabel("Frequência")
plt.legend()
plt.show()
