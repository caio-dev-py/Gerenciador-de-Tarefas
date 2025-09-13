# Gerenciador de Tarefas  

Projeto de **Gerenciador de Tarefas** desenvolvido em **Python** com **Flask**, utilizando **Poetry** para gerenciamento de dependências e ambiente virtual. A aplicação permite criar, editar e excluir tarefas, com autenticação de usuários e formulários seguros. O frontend foi construído com **HTML, CSS e Bootstrap**, e o projeto faz uso de **Flask-WTF, Flask-Login, Flask-SQLAlchemy** e **Python-Dotenv** para organização e segurança.  

## 🚀 Tecnologias utilizadas  
- Python  
- Flask  
- Flask-WTF  
- Flask-Login  
- Flask-SQLAlchemy  
- Python-Dotenv  
- HTML, CSS e Bootstrap  
- Poetry  

## 📂 Estrutura do projeto (exemplo)  
```
project/
│── src/ # Código principal da aplicação
│ ├── app.py # Ponto de entrada
│ ├── models.py # Modelos com SQLAlchemy
│ ├── forms.py # Formulários Flask-WTF
│ ├── routes/ # Rotas organizadas em blueprints
│ └── templates/ # HTML com Jinja2
│── static/ # Arquivos estáticos (CSS, JS, imagens)
│── .env # Variáveis de ambiente
│── pyproject.toml # Configuração do Poetry
│── README.md # Documentação do projeto
```

## ⚙️ Como rodar o projeto  
1. Clone este repositório:  
   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências do poetry:
    poetry install

3. Ative o ambiente virtual:
    poetry shell

4. Configura o arquivo **.env** com as variáveis abaixo:
    SECRET_KEY = ""

5. Execute a aplicação:
    python .\run.py

## ✅ Funcionalidades

1. Cadastro e autenticação de usuários
2. Criação, edição e exclusão de tarefas
3. Organização de tarefas em interface simples e responsiva
4. Integração entre backend (flask) e frontend (HTML, CSS, Bootstrap)