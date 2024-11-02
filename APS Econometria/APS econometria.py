import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
import numpy as np
import statsmodels.api as sm

# Carregar o arquivo Excel
file_path = 'C:/Users/User/Downloads/aps 2 - limpa - valores absolutos.xlsx'
data = pd.read_excel(file_path)

# Exibir as primeiras linhas do DataFrame e informações sobre as colunas
data.head(), data.info()

# Configurações para os gráficos
sns.set(style="whitegrid")

# Criar matriz apenas com os dados quantitativos
quant_data = data.drop(["Cor ou raça", "Nível de instrução mais elevado alcançado"], axis = 1)

# Criar matriz apenas com os dados qualitativos
quali_data = data.drop(["Renda mensal total", "Horas no trabalho doméstico", "Horas no trabalho não doméstico", "Idade", "Número de pessoas no domicílio"], axis = 1)
# Convertendo explicitamente para 'object' para garantir que são tratadas como dados categóricos
quali_data = quali_data.astype('object')

### Tabelas de análise descritiva

## Variáveis quantitativas

quant_columns = ["Renda mensal total", "Horas no trabalho doméstico", "Horas no trabalho não doméstico", "Idade", "Número de pessoas no domicílio"]

quant_descritive_stats = quant_data.describe()

# Adicionar Moda
quant_descritive_stats.loc['mode'] = quant_data.mode().iloc[0]

# Adicionar Skewness (Assimetria)
quant_descritive_stats.loc['skewness'] = quant_data.apply(skew)

# Adicionar Kurtosis (Curtose)
quant_descritive_stats.loc['kurtosis'] = quant_data.apply(kurtosis)

## Variáveis qualitativas

# Mapeamentos de acordo com as legendas fornecidas
mapa_instrucao = {
    1: 'Sem instrução e menos de 1 ano de estudo',
    2: 'Fundamental incompleto ou equivalente',
    3: 'Fundamental completo ou equivalente',
    4: 'Médio incompleto ou equivalente',
    5: 'Médio completo ou equivalente',
    6: 'Superior incompleto ou equivalente',
    7: 'Superior completo',
    'Não aplicável': 'Não aplicável'  # Este valor deve corresponder exatamente ao que está no seu DataFrame
}

mapa_cor_raca = {
    1: 'Branca',
    2: 'Preta',
    3: 'Amarela',
    4: 'Parda',
    5: 'Indígena',
    9: 'Ignorado'
}

# Aplicando as traduções
data['Nível de instrução mais elevado alcançado'] = data['Nível de instrução mais elevado alcançado'].replace(mapa_instrucao)
data['Cor ou raça'] = data['Cor ou raça'].replace(mapa_cor_raca)

# Estatísticas descritivas para cada variável qualitativa
estatisticas_instrucao = data['Nível de instrução mais elevado alcançado'].value_counts().to_frame()
estatisticas_cor_raca = data['Cor ou raça'].value_counts().to_frame()

# Calculando estatísticas para 'Nível de instrução mais elevado alcançado'
moda_instrucao = data['Nível de instrução mais elevado alcançado'].mode()[0]
frequencia_moda_instrucao = data['Nível de instrução mais elevado alcançado'].value_counts()[moda_instrucao]

# Calculando estatísticas para 'Cor ou raça'
moda_cor_raca = data['Cor ou raça'].mode()[0]
frequencia_moda_cor_raca = data['Cor ou raça'].value_counts()[moda_cor_raca]

# Criando a tabela combinada
tabela_combinada = pd.DataFrame({
    'Nível de Instrução': [moda_instrucao, frequencia_moda_instrucao],
    'Cor ou Raça': [moda_cor_raca, frequencia_moda_cor_raca]
}, index=['Moda', 'Frequência da Moda'])

# Tabelas individuais para cada variável
tabela_instrucao = estatisticas_instrucao
tabela_cor_raca = estatisticas_cor_raca

# Imprimindo as tabelas
print("Tabela Combinada de Variáveis Qualitativas:")
print(tabela_combinada)

print("\nTabela de Nível de Instrução:")
print(tabela_instrucao)

print("\nTabela de Cor ou Raça:")
print(tabela_cor_raca)

# Criar boxplots para cada variável qualitativa em relação à "Renda mensal total"
for column in quali_data.columns:
    plt.figure(figsize = (10, 6))
    sns.boxplot(x = column, y = 'Renda mensal total', data = data, palette = 'Set2')
    plt.title(f'Boxplot de {column} vs. Renda mensal total')
    plt.xticks(rotation = 30)
    plt.tight_layout()
    plt.show()

# Criar gráficos de dispersão para cada variável qualitativa em relação à "Renda mensal total"
for column in quali_data.columns:
    plt.figure(figsize = (10, 6))
    sns.scatterplot(x = column, y = 'Renda mensal total', data = data, hue = column, palette = 'Set2')
    plt.title(f'Dispersão de {column} vs. Renda mensal total')
    plt.xticks(rotation = 30)
    plt.legend(bbox_to_anchor = (1.05, 1), loc = 'upper left')
    plt.tight_layout()
    plt.show()


### Histogramas das variáveis quantitativas e matriz de correlações

# Configurações para os gráficos
sns.set(style = "whitegrid")

# Função para plotar histogramas
def plot_histogram(variable, color, title, binwidth = None, discrete = False):
    plt.figure(figsize = (8, 6))
    ax = sns.histplot(data[variable], kde = True, color = color, binwidth = binwidth, discrete = discrete)
    ax.set_title(title)
    ax.set_xlabel(title)
    ax.set_ylabel('Frequência')
    plt.show()

# Aplicando a função para cada variável
plot_histogram("Renda mensal total", 'green', 'Renda mensal total')
plot_histogram("Horas no trabalho doméstico", 'skyblue', 'Horas no trabalho doméstico')
plot_histogram("Horas no trabalho não doméstico", 'navy', 'Horas no trabalho não doméstico')
plot_histogram("Idade", 'gray', 'Idade')
plot_histogram("Número de pessoas no domicílio", 'orange', 'Número de pessoas no domicílio', binwidth=1, discrete=True)


# Matriz de correlação
correlation_matrix = quant_data.corr()
sns.heatmap(correlation_matrix, annot = True, cmap = 'coolwarm', fmt = ".2f")
plt.title('Matriz de Correlação entre as Variáveis')
plt.xticks(rotation = 35, ha = 'right')  # Rotação dos rótulos do eixo x para melhor visualização
plt.yticks(rotation = 0)  # Mantém os rótulos do eixo y sem rotação
plt.tight_layout()
plt.show()


# Função para plotar gráficos de dispersão e regressão
def plot_scatter_and_reg(x, color, title):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x, y="Renda mensal total", data=data, color=color)
    sns.regplot(x=x, y="Renda mensal total", data=data, scatter=False, color=color)
    plt.title(f'Renda mensal total vs. {title}')
    plt.xlabel(title)
    plt.ylabel('Renda mensal total')
    plt.tight_layout()
    plt.show()

# Aplicando a função para cada variável
plot_scatter_and_reg("Horas no trabalho doméstico", 'skyblue', 'Horas no trabalho doméstico')
plot_scatter_and_reg("Horas no trabalho não doméstico", 'darkblue', 'Horas no trabalho não doméstico')
plot_scatter_and_reg("Idade", 'grey', 'Idade')
plot_scatter_and_reg("Número de pessoas no domicílio", 'orange', 'Número de pessoas no domicílio')


# Função para plotar gráficos de resíduos
def plot_residuals(x, y, data, color, title):
    # Ajuste do modelo
    X = sm.add_constant(data[x])  # Adiciona uma constante ao modelo
    model = sm.OLS(data[y], X).fit()  # OLS = Ordinary Least Squares
    data['Previstos'] = model.predict(X)  # Valores previstos
    data['Resíduos'] = data[y] - data['Previstos']  # Cálculo dos resíduos

    # Gráfico de resíduos
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x = x, y = 'Resíduos', data = data, color = color)
    plt.axhline(y = 0, color = color, linestyle = '--')  # Linha horizontal no y = 0
    plt.title(f'Resíduos de {title}')
    plt.xlabel(x)
    plt.ylabel('Resíduos')
    plt.tight_layout()
    plt.show()

# Plotando gráficos de resíduos para cada variável independente
plot_residuals('Horas no trabalho doméstico', 'Renda mensal total', data, 'skyblue', 'Horas no trabalho doméstico vs. Renda mensal total')
plot_residuals('Horas no trabalho não doméstico', 'Renda mensal total', data, 'darkblue', 'Horas no trabalho não doméstico vs. Renda mensal total')
plot_residuals('Idade', 'Renda mensal total', data, 'grey', 'Idade vs. Total Renda mensal total')
plot_residuals('Número de pessoas no domicílio', 'Renda mensal total', data, 'orange', 'Número de pessoas no domicílio vs. Renda mensal total')


## Percentis de cada categoria das variáveis qualitativas - de 10 em 10%

# Calcular os percentis do Nível de Instrução mais Elevado
categories_instrucao = data['Nível de instrução mais elevado alcançado'].unique()
percentiles_data_instrucao = {}
for category in categories_instrucao:
    category_data = data[data['Nível de instrução mais elevado alcançado'] == category]["Renda mensal total"]
    percentiles_data_instrucao[category] = np.percentile(category_data, np.arange(0, 101, 10))

# Converter o dicionário em DataFrame
percentiles_df_instrucao = pd.DataFrame(percentiles_data_instrucao, index=[f'Percentil {i}' for i in np.arange(0, 101, 10)])

# Exibir a tabela de percentis para o Nível de Instrução mais Elevado
print("Tabela de Percentis do Nível de Instrução mais Elevado:")
print(percentiles_df_instrucao)
print("\n")

# Calcular os percentis da Cor ou Raça
categories_cor_raca = data['Cor ou raça'].unique()
percentiles_data_cor_raca = {}
for category in categories_cor_raca:
    category_data = data[data['Cor ou raça'] == category]["Renda mensal total"]
    percentiles_data_cor_raca[category] = np.percentile(category_data, np.arange(0, 101, 10))

# Converter o dicionário em DataFrame
percentiles_df_cor_raca = pd.DataFrame(percentiles_data_cor_raca, index=[f'Percentil {i}' for i in np.arange(0, 101, 10)])

# Exibir a tabela de percentis para a Cor ou Raça
print("Tabela de Percentis da Cor ou Raça:")
print(percentiles_df_cor_raca)




