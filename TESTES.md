# Testes - Conversor de Temperatura

## Casos de Teste

| ID | Entrada | Saída Esperada | Status |
|----|---------|--------|--------|
| TC-01 | GET / | Página com formulário | PASS |
| TC-02 | POST temp=0 | 0 °C = 32 °F | PASS |
| TC-03 | POST temp=25 | 25 °C = 77 °F | PASS |
| TC-04 | POST temp=100 | 100 °C = 212 °F | PASS |
| TC-05 | POST temp=-40 | -40 °C = -40 °F | PASS |
| TC-06 | POST temp="abc" | "Informação inválida" | PASS |
| TC-07 | POST temp="" | "Informação inválida" | PASS |

## Testes Manuais

**Teste de Interfere**:
1. Abra http://localhost:5000
2. Digite um valor (ex: 25)
3. Clique "Calcular"
4. Verifique o resultado (deve ser 77)

**Teste de Erro**:
1. Abra http://localhost:5000
2. Digite "abc"
3. Clique "Calcular"
4. Verifique mensagem de erro em vermelho

## Performance

- Tempo de resposta: ~20-50ms
- Sem banco de dados
- Aplicação leve e rápida

---

**Versão**: 1.0
