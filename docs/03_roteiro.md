# Roteiro público da migração

O proprietário implementará o banco e a aplicação. Este roteiro registra a sequência pretendida; cada etapa depende de conferência com exemplos reais no ambiente privado.

| Etapa | Entrega | Critério de conferência |
|---|---|---|
| 1. Regras e amostras | Contratos de pedido, item, extrato e compra; decisões de custo e status. | Casos de cancelamento, estorno, compra fracionada e combo entendidos. |
| 2. Modelo lógico | Entidades, chaves, relações, vigência e permissões. | Nenhuma chave central depende de posição em planilha ou nome livre. |
| 3. Banco de teste | Migrações reproduzíveis, restrições, funções e políticas de acesso. | Base vazia pode ser criada novamente e rejeita dados inválidos. |
| 4. Importadores | Leitura XML/JSON e adaptador histórico, com lote e fila de rejeições. | Reimportação não duplica fatos e mantém rastreabilidade. |
| 5. Estoque e compras | Contagem inicial, movimentos, fornecedores, cotações e custo médio. | Saldo por loja e item fecha com movimentos e contagens. |
| 6. Conciliação | Pedidos, eventos e extratos associados. | Diferenças ficam identificadas; pagamento depende de evidência. |
| 7. Financeiro e preço | Contas, DRE, fluxo, capital de giro e cenários de promoção. | Totais conciliados por período, loja e canal. |
| 8. Interface e painéis | Fluxos operacionais em Python. | Operação e revisão podem ser feitas sem a planilha. |
| 9. Operação paralela | Comparação controlada entre legado e sistema novo. | Divergências documentadas e critério de virada aprovado. |
| 10. Banco/Open Finance | Integração opcional após conciliação da plataforma. | Transações bancárias ligadas a repasses sem perder a origem. |

## Questões ainda abertas

- Tratamento de devoluções, compras retroativas e estoque negativo no custo médio móvel.
- Semântica de cancelamentos, estornos parciais, taxas e ajustes em cada plataforma.
- Critério de sugestão de compras: cobertura, prazo, embalagem e limite financeiro.
- Papéis de usuário e escopo de acesso por loja.
- Contratos efetivamente disponíveis para integração automatizada com cada plataforma.

Decisões, testes e exemplos com dados reais pertencem ao ambiente privado. No repositório público, casos de demonstração usarão dados sintéticos.
