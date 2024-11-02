# APS - Finanças III: Aplicações com Opções (Calls e Puts) e Gestão de Riscos

Este projeto explora o uso de derivativos financeiros na gestão de risco, aplicando opções de compra (calls) e venda (puts) no contexto do caso da Porsche. As análises incluem a automatização de cálculos de payoff e retorno de opções e o cálculo de Value at Risk (VaR) para medir o risco cambial da empresa. As implementações são feitas em Python, e as aplicações desenvolvidas servem para auxiliar o CFO a tomar decisões informadas sobre hedge e exposição cambial. Aqui, você encontrará os dois arquivos em .py, o relatório em Word e a base de dados usada.

## Estrutura do Projeto

### Objetivos

1. **Entender o uso de derivativos no gerenciamento de risco** - O case da Porsche exemplifica o uso de opções e operações de hedge cambial para proteger receitas contra a volatilidade do mercado.
2. **Automatizar cálculos de Payoff e Retorno de Opções** - Implementação em Python para cálculo e visualização de payoff e retorno de calls e puts.
3. **Cálculo de Value at Risk (VaR)** - Implementação de simulações Monte Carlo para estimar o VaR das receitas expostas ao câmbio, com horizonte de 1 ano e nível de confiança de 95%.

### Estrutura das Aplicações

#### Aplicação 1: Cálculo de Payoff de Opções
   - **Descrição:** Desenvolvemos um script em Python que permite ao usuário inserir dados de opções (calls ou puts) e, em seguida, calcula o payoff para um intervalo de preços de exercício (Strike).
   - **Entrada:** Preço de exercício, prêmio, e tipo de opção (call ou put).
   - **Saída:** Gráficos e tabelas com o retorno da estratégia para diferentes valores de preços de vencimento (St).
   - **Uso:** Auxilia o CFO a visualizar o payoff de diferentes opções e entender melhor o impacto de calls e puts em várias condições de mercado.

#### Aplicação 2: Cálculo de Value at Risk (VaR)
   - **Descrição:** Implementamos um modelo em Python que usa simulações Monte Carlo para calcular o VaR das receitas da Porsche, considerando a exposição cambial. O VaR estimado fornece uma medida da perda máxima esperada, com 95% de confiança, ao longo de um ano.
   - **Entrada:** Dados históricos da taxa de câmbio EUR/USD.
   - **Saída:** Valor do VaR (em euros) e um gráfico de distribuição de perdas potenciais.
   - **Uso:** Oferece uma medida de risco que ajuda a Porsche a entender melhor a exposição de suas receitas ao câmbio e a tomar decisões informadas sobre hedge.

## Como Executar

1. **Requisitos**: Instale as bibliotecas necessárias, incluindo `numpy`, `pandas`, e `matplotlib`.
2. **Scripts**: Execute `aplicacao1.py` para cálculos de payoff e `aplicacao2.py` para cálculos de VaR.
3. **Entrada de Dados**: Siga as instruções nos scripts para inserir os valores das opções e taxas de câmbio.
4. **Saídas e Interpretação**: Os scripts geram tabelas e gráficos automaticamente para facilitar a interpretação dos resultados.

## Estrutura de Arquivos

- **aplicacao1.py** - Script para cálculo e visualização de payoff de opções.
- **aplicacao2.py** - Script para cálculo de Value at Risk (VaR) utilizando simulações Monte Carlo.
- **dados/** - Diretório onde os arquivos de dados históricos de câmbio devem ser armazenados.
- **relatorio.docx** - Relatório com todas as análises, gráficos, tabelas, e explicações do caso Porsche.

## Referências

- Case “Hedging at Porsche” (Michigan Ross School of Business – WDI Publishing)
- Documentação Bloomberg e CapitalIQ para coleta de dados financeiros.

---

## Contribuições

Contribuições são bem-vindas! Para sugestões ou melhorias, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto está licenciado sob a licença MIT.
