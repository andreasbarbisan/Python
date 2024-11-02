#APS1 - Finanças

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df1 = pd.read_excel('C:\\Andreas\\Insper\\Semestre 3\\Finanças 1\\APS\\Cópia de Klabin aps.xlsx', sheet_name="Graficos")

x = pd.to_datetime(df1.iloc[:, 0], format='%Y')
y = pd.to_numeric(df1.iloc[:, 9], errors='coerce') / 1e6  
y2 = pd.to_numeric(df1.iloc[:, 10], errors='coerce') / 1e6  

sns.set(style="darkgrid")
plt.figure(figsize=(8, 5))

sns.lineplot(x=x, y=y, label="Ativo Circulante")
sns.lineplot(x=x, y=y2, label="Ativo Não Circulante")

def millions(x, pos):
    return f'{x:.1f}M'

ax = plt.gca()
ax.yaxis.set_major_formatter(FuncFormatter(millions))

plt.xlabel('Anos (após 2023, valores projetados pelo grupo)', fontsize = 20)
plt.ylabel('Valores ($BRL em milhões)', fontsize = 20)
plt.title('Projeção dos ativos da Klabin', fontsize = 20)

plt.xticks(fontsize = 20)
plt.yticks(fontsize=20)

plt.legend(fontsize = 20)

plt.show()