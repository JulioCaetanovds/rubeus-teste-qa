# Teste Prático QA - Rubeus

Este repositório contém a resolução do teste prático para a vaga de QA, focado em garantir a qualidade e a melhor experiência do usuário nas plataformas da Rubeus.

O projeto une análise exploratória detalhada com uma suíte de automação moderna e robusta.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.14+
- **Framework de Teste:** Pytest
- **Ferramenta de Automação:** Playwright
- **Dados Dinâmicos:** Faker (para geração de massa de teste aleatória e realista)
- **Documentação:** Markdown

## 📂 Estrutura do Projeto

O repositório está organizado da seguinte forma:

1. **Testes Exploratórios**: Relatórios técnicos contendo bugs de funcionalidade, inconsistências de UI e melhorias de UX.
   - [Página de Certificação](./testes_exploratorios/certificacao.md)
   - [Página do Site](./testes_exploratorios/site.md)
2. **Testes Automatizados**: Scripts de automação para os fluxos de maior impacto.
   - `test_certificacao.py`: Fluxos de inscrição e validação de erros.
   - `test_site.py`: Newsletter e CTAs do carrossel.
   - `test_smoke.py`: Integridade de links e navegação entre páginas.
   - `test_ux_validation.py`: Testes de responsividade mobile e validação de máscaras de campos.

## 🚀 Como Rodar a Automação

**1. Acesse a pasta do projeto e ative o ambiente virtual:**
```bash
cd testes_automatizados
python -m venv venv
# No Windows:
venv\Scripts\activate
```

**2. Instale as dependências:**
```bash
pip install pytest-playwright faker
playwright install
```

**3. Execute a suíte de testes:**
```bash
pytest --headed
```

## 🧠 Notas Técnicas (Leitura do QA)

A suíte de testes foi configurada para refletir o estado real da aplicação. Note que alguns testes resultarão no status **XFAIL (Expected Fail)**:

* **Validação de Telefone:** O teste falha pois o sistema permite a entrada de caracteres alfabéticos em campos numéricos.
* **Menu Mobile:** O teste de responsividade falha pois o site não exibe o menu "hambúrguer" em resoluções mobile, apenas comprime os elementos de desktop.

O uso do `xfail` demonstra a detecção automatizada de bugs conhecidos sem interromper a integridade da execução da suíte.

## 🏁 Metodologia de Reporte
Todos os itens reportados nos testes exploratórios seguem a estrutura:
- **Tipo:** Correção, Nova funcionalidade ou Melhoria.
- **Classificação:** Utilidade, Usabilidade ou Desejabilidade.
- **Prioridade:** Baseada no impacto direto na conversão e na experiência do usuário final.