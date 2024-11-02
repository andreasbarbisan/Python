#APS1 - Finanças

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_excel('C:\\Andreas\\Insper\\Semestre 3\\Finanças 1\\APS\\Cópia de Klabin aps.xlsx', sheet_name="Graficos")

x = df1.iloc[:,0]
y = df1.iloc[:,3]
y2 = df1.iloc[:,4]

sns.set(style="darkgrid")
plt.figure(figsize=(8,5))


sns.lineplot(x=x, y=y, label = "ROA")
sns.lineplot(x=x, y=y2, label = "ROE")

plt.xticks(np.arange(min(x), max(x) + 1, 1))

plt.xlabel('Anos (dados após 2023 são projetados pelo grupo)', fontsize = 20)
plt.ylabel('Valores (% p.p.)', fontsize = 20)
plt.title('Variação ROA e ROE Klabin', fontsize = 20)

plt.xticks(fontsize = 20)
plt.yticks(fontsize=20)

plt.legend(fontsize = 20)

plt.show()