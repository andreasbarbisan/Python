# APS - Finanças 2: Seleção de Portfólio Ótima para Diferentes Perfis de Investidores

Este projeto foi desenvolvido para criar uma seleção de portfólio ótima que atenda a três perfis distintos de investidores: agressivo, moderado e conservador. O trabalho utiliza a metodologia de fronteira eficiente de Markowitz e outros conceitos de finanças modernas para identificar a combinação de ativos que maximiza o retorno ajustado ao risco de acordo com o perfil de cada investidor. Aqui, você vai encontrar o arquivo em .py, o relatório em Word e a base de dados utilizada.

## Estrutura do Projeto

### Objetivos

1. **Construir uma carteira de investimentos diversificada** - A seleção inclui ativos nacionais e internacionais para minimizar o risco através da diversificação.
2. **Aplicar técnicas de otimização de portfólio** - Utilização da fronteira eficiente e cálculo da carteira de mínima variância e do índice de Sharpe para determinar a carteira de risco ótima.
3. **Analisar perfis de investidores** - Três carteiras foram desenvolvidas para diferentes graus de aversão ao risco, representando perfis agressivo, moderado e conservador.

### Metodologia e Ferramentas

- **Cálculo da Matriz de Covariância**: Usada para entender as correlações entre os ativos e auxiliar na diversificação da carteira.
- **Simulações em Python**: Foram realizadas 1 milhão de simulações para calcular o retorno e o risco de diversas combinações de pesos entre os ativos selecionados.
- **Fronteira Eficiente e Carteira de Mínima Variância**: Determinação da fronteira eficiente e da carteira de mínima variância através do método de minimização `optimize.minimize` da biblioteca Scipy.
- **Índice de Sharpe**: Cálculo do índice para cada combinação de pesos dos ativos a fim de identificar a carteira com o melhor retorno ajustado ao risco.
- **Alocação para Diferentes Perfis**: Utilizamos uma fórmula baseada na aversão ao risco para calcular as alocações ótimas para os perfis de investidores: agressivo, moderado e conservador.

### Perfis dos Investidores

- **Agressivo (Baixa Aversão ao Risco)**: Propenso a assumir mais risco para obter retornos mais altos.
- **Moderado (Média Aversão ao Risco)**: Equilíbrio entre risco e retorno.
- **Conservador (Alta Aversão ao Risco)**: Preferência por uma carteira com menor risco, mesmo que o retorno seja mais modesto.

## Conteúdo do Projeto

- **Código em Python**: O script `codigo.py` executa todas as etapas de simulação e otimização, desde o cálculo da matriz de covariância até a geração da fronteira eficiente e da carteira ótima para cada perfil.
- **Relatório**: Documento que detalha a justificativa dos ativos selecionados, a metodologia e os principais resultados das análises.
- **Base de Dados**: Inclui os retornos históricos dos ativos escolhidos, assim como o ativo livre de risco utilizado nas simulações.

## Como Executar

1. **Requisitos**: Certifique-se de ter as bibliotecas `numpy`, `pandas`, `matplotlib` e `scipy` instaladas.
2. **Execução do Script**: Rode o script principal (`codigo.py`) para gerar as simulações e visualizações da fronteira eficiente, carteira de mínima variância e perfis de portfólio para os diferentes tipos de investidores.
3. **Saída do Script**: O script exibirá gráficos e os valores dos índices de Sharpe, retornos esperados e volatilidade para cada perfil.

## Estrutura de Arquivos

- **codigo.py**: Script com o código completo em Python.
- **relatorio.pdf**: Documento explicativo sobre a montagem do portfólio e as escolhas de ativos.
- **dados.xlsx**: Base de dados com os retornos históricos dos ativos.

## Referências

- Bodie, Z., Kane, A., & Marcus, A. J. *Investimentos*, 10ª edição, Bookman, 2014.
- Markowitz, H. *Portfolio Selection*, The Journal of Finance, Vol. 7, No. 1, pp. 77-91, 1952.

---

## Contribuições

Sugestões e melhorias são bem-vindas! Para contribuir, abra uma *issue* ou envie um *pull request*.

## Licença

Este projeto está licenciado sob a licença MIT.
