# Teste Prático QA - RBS

Este repositório contém a resolução do teste prático para a vaga de QA, focado em garantir a qualidade e a melhor experiência do usuário nas plataformas da RBS. 

O projeto engloba testes exploratórios detalhados e automação de fluxos críticos utilizando tecnologias modernas.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.14+
- **Framework de Teste:** Pytest
- **Ferramenta de Automação:** Playwright
- **Dados Dinâmicos:** Faker (para geração de dados aleatórios de massa de teste)
- **Documentação:** Markdown

## 📂 Estrutura do Projeto

O repositório está organizado da seguinte forma:

1. **Testes Exploratórios**: Relatórios técnicos contendo bugs de funcionalidade, inconsistências de UI e melhorias de UX.
   - [Página de Certificação](./testes_exploratorios/certificacao.md)
   - [Página do Site](./testes_exploratorios/site.md)
2. **Testes Automatizados**: Scripts de automação para os fluxos de maior impacto.
   - Validação de CTAs (botões) inativos.
   - Validação de falhas críticas no envio de formulários (Newsletter e Inscrição).

## 🚀 Como Rodar a Automação

**1. Acesse a pasta do projeto:**
```bash
cd testes_automatizados
```

**2. Crie e ative o ambiente virtual:**
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
```

**3. Instale as dependências:**
```bash
pip install pytest-playwright faker
playwright install
```

**4. Execute os testes:**
```bash
pytest --headed
```

## 🧠 Metodologia de Reporte
Todos os itens reportados nos testes exploratórios seguem a estrutura:

* **Tipo:** Correção, Nova funcionalidade ou Melhoria.
* **Classificação:** Utilidade, Usabilidade ou Desejabilidade.
* **Prioridade:** Baseada no impacto direto no negócio e na experiência do usuário.

---

### 🏁 Próximos Passos para Entrega:
1. **Commit e Push:** Suba todas as alterações para o seu GitHub.
2. **Organize as Imagens:** Garanta que os prints estejam na pasta `testes_exploratorios/imagens/` com os nomes citados nos arquivos .md.
3. **Validação Final:** Verifique se o link do repositório está público para que os recrutadores consigam acessar.