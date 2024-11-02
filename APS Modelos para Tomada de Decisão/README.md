# APS 3 - Modelos para Tomada de Decisão: Dinâmica de Sistemas e Simulação de Monte Carlo

Este projeto aplica conceitos de Dinâmica de Sistemas e Simulação de Monte Carlo para analisar a viabilidade econômica de um investimento em produção de embalagens sustentáveis pela empresa Klabin. O estudo examina o equilíbrio entre oferta e demanda, a tendência de substituição entre diferentes tipos de fibras, e a projeção de receitas e custos, com um foco em avaliação de risco e retorno financeiro.

## Estrutura do Projeto

### Objetivos

1. **Equilíbrio entre Oferta e Demanda**: Estimar a variação de preço com base no equilíbrio entre demanda e oferta de embalagens.
2. **Simulação de Substituição de Material**: Modelar a transição entre o uso de fibra longa e Eukaliner em embalagens, analisando a viabilidade econômica de diferentes proporções.
3. **Simulação de Monte Carlo para VPL e TIR**: Estimar o Valor Presente Líquido (VPL) e a Taxa Interna de Retorno (TIR) do projeto, utilizando simulação de Monte Carlo para capturar incertezas nos preços de insumos e câmbio.

### Metodologia

- **Dinâmica de Sistemas**: Utilizamos equações diferenciais para modelar o equilíbrio de preço e a substituição entre tipos de fibras ao longo do tempo.
- **Simulação de Monte Carlo**: Realizamos simulações para estimar VPL e TIR, incorporando variabilidade nos preços de venda, demanda e câmbio.
- **Avaliação Financeira**: Calculamos o fluxo de caixa do projeto considerando depreciação, custo de fabricação, armazenamento e vendas projetadas, além do impacto fiscal.

### Código e Estrutura de Arquivo

- **APS3_modelos.py**: Código Python que implementa todos os cálculos e simulações. As principais funções incluem:
  - Modelagem da variação de preço com equilíbrio entre oferta e demanda.
  - Cálculo da substituição entre fibras e simulação da proporção de Eukaliner.
  - Simulação de Monte Carlo para estimar o VPL e a TIR.
- **Parâmetros Importantes**:
  - `gamma`: coeficiente de variação de preço.
  - `θ`: taxa de transição para Eukaliner.
  - Parâmetros financeiros, como taxa de depreciação, investimento inicial e taxa de câmbio.

### Resultados

1. **Equilíbrio de Preço e Demanda**: Identificamos o ponto de equilíbrio de preço ao longo do tempo com base na oferta e demanda projetadas.
2. **Proporção de Eukaliner**: Projeção da transição de fibra longa para Eukaliner, com impacto nas decisões de fabricação.
3. **Distribuição de VPL e TIR**: A simulação de Monte Carlo fornece uma distribuição do VPL e da TIR, auxiliando na avaliação do risco e retorno esperados do projeto.

## Como Executar

1. **Requisitos**: Certifique-se de ter as bibliotecas `numpy`, `matplotlib`, `scipy`, e `numpy_financial`.
2. **Execução**: Execute o arquivo `APS3_modelos.py` para gerar os resultados e gráficos de VPL, TIR e projeção de preços e demanda.
3. **Interpretação**: Os gráficos gerados incluem a distribuição dos VPLs simulados e a variação esperada de preços e proporções ao longo do tempo.

## Referências

- Material da disciplina Modelos para Tomada de Decisão, Insper.
- Dados históricos de preços e câmbio utilizados para projeções e simulações.

---

## Contribuições

Sugestões para melhorias são bem-vindas! Abra uma *issue* ou envie um *pull request*.

## Licença

Este projeto está licenciado sob a licença MIT.
