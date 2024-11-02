# APS 2 - Finanças I: Análise de Investimento da Klabin com Simulação de Monte Carlo

Este projeto realiza uma análise de viabilidade de investimento no projeto da máquina MP29 para produção de Eukaliner pela Klabin S/A. A análise inclui projeções de fluxo de caixa, cálculo de VPL, TIR e Payback Descontado, bem como uma simulação de Monte Carlo para avaliar o risco financeiro em diferentes cenários de variação de preço e câmbio.

## Objetivos

1. **Calcular o Fluxo de Caixa**: Estimar a receita e os custos do projeto ao longo de 5 anos, incluindo depreciação e impostos.
2. **Calcular VPL, TIR e Payback Descontado**: Avaliar a viabilidade econômica do projeto com base nesses indicadores financeiros.
3. **Simulação de Monte Carlo**: Realizar 100.000 simulações para capturar variações no preço de venda do Eukaliner e na taxa de câmbio USD/BRL, gerando uma distribuição de possíveis valores para o VPL.

## Metodologia e Ferramentas

- **Simulação de Monte Carlo**: O código usa distribuições normais para modelar o preço do Eukaliner e a taxa de câmbio. 
- **Bibliotecas Utilizadas**: `numpy`, `matplotlib`, `numpy_financial`.
- **Parâmetros**: Custos e quantidades fornecidos pela análise do projeto, com depreciação anual de R$437.500.000.

## Estrutura do Código

- **Parâmetros de Entrada**: Preço de venda, custo de produção, taxa de câmbio e taxas de depreciação e impostos.
- **Cálculo do Fluxo de Caixa**: Receitas, CMV, LAJIR, NOPAT e FCO são calculados para cada ano.
- **Simulação de Monte Carlo**: Resultados do VPL para diferentes cenários são apresentados em um histograma.

## Como Executar

1. **Instale os Pacotes**: Certifique-se de ter `numpy`, `matplotlib`, e `numpy_financial` instalados.
2. **Execute o Código**: O script `APS2_fin1.py` gera uma distribuição do VPL com 100.000 simulações.
3. **Interprete os Resultados**: O histograma exibe a frequência de valores do VPL, com uma linha indicando o ponto de equilíbrio (VPL = 0).

---

## Contribuições

Contribuições e sugestões são bem-vindas! Para melhorias, abra uma *issue* ou envie um *pull request*.

## Licença

Este projeto está licenciado sob a licença MIT.
