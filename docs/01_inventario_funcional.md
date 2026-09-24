# Inventário funcional do sistema legado

O sistema atual usa planilhas, consultas Power Query e macros VBA para reunir arquivos de plataformas, registrar operações e montar relatórios. Este inventário descreve funções, sem expor dados ou regras comerciais específicas da operação.

| Área atual | O que faz | Destino proposto |
|---|---|---|
| Vendas | Consolida pedidos, produtos vendidos e valores por canal. | Pedidos, itens e eventos financeiros separados; identificadores externos preservados como texto. |
| Repasses | Projeta valores e datas a receber. | Conciliação com extrato efetivo, mantendo previsto e realizado distintos. |
| Estoque | Cadastra insumos, unidades, custo e entradas/saídas. | Cadastro de itens e livro de movimentos por loja, com contagem de abertura. |
| Compras | Lê documentos de fornecedores e auxilia a cotação. | Documento, itens, fornecedor, SKU externo e pedido de compra ligados por IDs estáveis. |
| Ficha técnica | Relaciona produto vendável aos insumos consumidos. | Receitas versionadas, com unidade e quantidade por componente. |
| Combos | Agrupa itens vendáveis em uma oferta. | Composição de combo separada da ficha técnica; registrar substituições escolhidas no pedido. |
| Custo e preço | Calcula custo do produto, preço, taxas e margem. | Histórico de custo e regras de preço por canal e vigência; cenários de volume previsto e real. |
| Financeiro | Organiza obrigações, recebíveis e relatórios. | Contas, parcelas e pagamentos explícitos; DRE, caixa e capital de giro derivados de eventos classificados. |
| Painéis | Exibe indicadores consolidados. | Consultas e interface com filtros, detalhamento e trilha de origem. |

## O que permanece, muda ou sai

**Permanece como função de negócio:** conciliação de vendas e repasses, controle de estoque, compras, ficha técnica, combos, contas, relatórios e precificação.

**Muda de implementação:** importações viram pipelines verificáveis; cálculos viram regras versionadas; lançamentos passam a ter origem e reversão; telas substituem formulários e tabelas dinâmicas.

**Sai como dependência operacional:** números de linha como identificador, cópia manual entre abas, status deduzido apenas pela passagem da data, caminhos de arquivo fixos e reprocessamento baseado somente na última data vista.

## Regras de preservação

1. O pedido e cada item devem manter vínculo com a plataforma e seu identificador de origem.
2. O consumo de estoque parte do item efetivamente vendido e da versão da receita aplicável.
3. Uma entrada, saída, estorno ou ajuste deve ter evento de origem e não deve duplicar ao reimportar.
4. Um recebível só é marcado como liquidado mediante evidência de repasse.
5. A contagem física define a abertura do estoque na virada; os movimentos posteriores explicam o saldo.

Este documento é um inventário funcional público, não uma reprodução das fórmulas ou dos dados do legado.
