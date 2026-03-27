# Conversor de Temperatura - Documentação Acadêmica

## 1. Introdução

Conversor de temperatura simples desenvolvido em Python com Flask. A aplicação converte graus Celsius (°C) para Fahrenheit (°F) através de uma interface web.

## 2. Tecnologias

- **Python** 3.x - Backend
- **Flask** - Framework web
- **HTML5** - Frontend
- **Pico CSS** - Estilização responsiva

## 3. Estrutura do Projeto

```
📁 WebII_Conversor_de_temperatura/
├── app.py                 # Código principal (Flask)
├── templates/
│   └── index.html        # Interface web
└── venv/                 # Ambiente virtual
```

## 4. Como Executar

### Instalação
```bash
# 1. Ativar ambiente virtual (Windows)
.\venv\Scripts\Activate.ps1

# 2. Instalar Flask (se necessário)
pip install flask

# 3. Executar aplicação
python app.py

# 4. Acessar
# http://localhost:5000
```

## 5. Funcionalidades

- Conversão de °C para °F
- Validação de entrada (aceita números com decimais)
- Tratamento de erros com mensagens claras
- Interface responsiva e intuitiva

## 6. Fórmula de Conversão

```
Fahrenheit = (Celsius × 1.8) + 32
```

### Exemplos
| Celsius | Fahrenheit |
|---------|-----------|
| 0 | 32 |
| 25 | 77 |
| 100 | 212 |

## 7. Funcionamento Técnico

### Backend (app.py)
- **GET /**: Carrega página inicial
- **POST /**: Processa conversão
- Valida entrada com try-except
- Renderiza resultado com Jinja2

### Frontend (index.html)
- Formulário com campo de entrada
- Botão para enviar dados
- Exibição de resultado ou erro
- Estilização com Pico CSS

## 8. Tratamento de Erros

| Entrada | Resultado |
|---------|-----------|
| "25" | 77°F ✓ |
| "-40" | -40°F ✓ |
| "abc" | Erro ✗ |
| "" | Erro ✗ |

## 9. Fluxo de Operação

```
1. Usuário acessa localhost:5000
   ↓
2. Página carrega com formulário vazio
   ↓
3. Usuário digita temperatura em °C
   ↓
4. Clica botão "Calcular"
   ↓
5. Dados enviados via POST
   ↓
6. Flask valida e converte
   ↓
7. Resultado exibido na página
```

## 10. Requisitos Funcionais

- ✓ Converter temperatura de °C para °F
- ✓ Aceitar entrada numérica do usuário
- ✓ Validar dados de entrada
- ✓ Exibir resultado ou mensagem de erro
- ✓ Interface responsiva

## 11. Requisitos Não-Funcionais

- ✓ Tempo de resposta < 100ms
- ✓ Código legível e comentado
- ✓ Sem erros ou crashes
- ✓ Funcionar em navegadores modernos

## 12. Limitações

- Apenas conversão °C → °F
- Sem histórico ou persistência de dados
- Sem autenticação
- Aplicação local (sem deploy)

## 13. Conclusão

Projeto simples que demonstra integração entre frontend e backend em aplicação web. Implementa conceitos fundamentais de desenvolvimento web usando Python e Flask.

---

**Versão**: 1.0  
**Data**: Março 2026  
**Disciplina**: Programação Web II