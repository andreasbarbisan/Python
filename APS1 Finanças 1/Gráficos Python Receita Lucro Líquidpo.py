#APS1 - Finanças

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df1 = pd.read_excel('C:\\Andreas\\Insper\\Semestre 3\\Finanças 1\\APS\\Cópia de Klabin aps.xlsx', sheet_name="Graficos")

x = pd.to_datetime(df1.iloc[:, 0], format='%Y')
y = df1.iloc[:, 1]
y2 = df1.iloc[:, 2]

sns.set(style="darkgrid")
plt.figure(figsize=(8, 5))

sns.lineplot(x=x, y=y, label="Receita")
sns.lineplot(x=x, y=y2, label="Lucro Líquido")

def millions(x, pos):
    return f'{x / 1e6:.1f}M'

ax = plt.gca()
ax.yaxis.set_major_formatter(FuncFormatter(millions))

plt.xlabel('Anos (dados após 2023 são projetados pelo grupo)', fontsize = 20)
plt.ylabel('Valores ($BRL em milhares)', fontsize = 20)
plt.title('Crescimento das receitas e lucros da Klabin', fontsize = 20)

plt.xticks(fontsize = 20)
plt.yticks(fontsize=20)

plt.legend(fontsize = 20)


plt.show()
