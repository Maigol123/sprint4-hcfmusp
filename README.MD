# 🏥 Sistema de Gerenciamento de Consultas - HCFMUSP  
**Disciplina:** Computational Thinking Using Python  
**Sprint 4 – FIAP (2025)**  

Este projeto tem como objetivo integrar um CRUD Python com um **banco de dados SQLite** e disponibilizar uma **API Flask** com interface web.  
O sistema simula o gerenciamento de **consultas médicas**, **parentes de emergência** e **lembretes automáticos** do Hospital das Clínicas (HCFMUSP).  

---

## 🚀 Funcionalidades Principais

✅ **CRUD completo** para:
- Consultas  
- Parentes/Contatos  
- Lembretes  

✅ **Integração com Banco de Dados (SQLite)**  
Os dados são carregados automaticamente a partir do arquivo `dados_iniciais.json` na primeira execução.

✅ **Exportação para JSON**  
Permite exportar todos os registros do banco em um arquivo `.json`.

✅ **Consumo de API Externa Pública**  
O sistema importa médicos fictícios da API `https://jsonplaceholder.typicode.com/`.

✅ **Interface Web Simples (HTML + JavaScript)**  
Frontend conectado ao backend Flask para interação direta com os dados.

---

## 📂 Estrutura do Projeto

```bash
SPRINT 4/
│
├── app.py                  # Código principal: rotas Flask, inicialização do banco e API
├── models.py               # Definição das tabelas (Consultas, Parentes, Lembretes)
├── dados_iniciais.json     # Dados de exemplo (base importada do Challenge.py)
├── requirements.txt        # Dependências do projeto (Flask, SQLAlchemy, Requests)
├── .gitignore              # Ignora venv, banco de dados e arquivos temporários
│
├── instance/               # Pasta criada automaticamente pelo Flask
│   └── db.sqlite3          # Banco de dados SQLite gerado ao rodar o sistema
│
└── static/                 # Arquivos do front-end
    └── index.html          # Página web simples (listar, exportar e importar dados)

👨‍💻 Integrantes

Nome | RM | Função
Miguel Oliveira Dias(RM:565492)	Desenvolvimento Python, integração Flask e vídeo
(Lucas Barranha Giannini)(RM:564508) Banco de Dados e Testes
(João Victor De Sousa)(RM:560907) Interface Web e Documentação