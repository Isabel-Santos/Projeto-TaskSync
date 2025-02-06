# Projeto-TaskSync

TaskSync é um sistema distribuído de gerenciamento de tarefas desenvolvido com Flask no backend e React no frontend. O projeto permite a criação, edição e gerenciamento de tarefas com autenticação JWT, armazenando os dados em um banco de dados relacional.

## 1. Requisitos

Antes de iniciar, certifique-se de ter os seguintes softwares instalados:

- Python 3.x
- Node.js 16+ e npm 8+
- Git para clonagem do repositório

Caso ainda não tenha essas dependências instaladas:

- Baixe o Python
- Instale o Node.js e npm
- Instale o Git

## 2. Configuração do Backend (Flask)

### 2.1 Clonar o repositório
```bash
git clone https://github.com/Isabel-Santos/projeto-tasksync.git
cd projeto-tasksync
```

2.2 Criar e ativar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

2.3 Instalar dependências do backend
```bash
pip install -r requirements.txt
```

2.4 Executando o Backend
Para rodar o backend, execute o seguinte comando:
```bash
python run.py
```
Isso vai iniciar o servidor Flask, geralmente na URL http://127.0.0.1:5000/.

3. Configuração do Frontend (React)
3.1 Navegar até a pasta do frontend
Abra um novo terminal e navegue até o diretório frontend:
```bash
cd app/frontend
```
Instale as dependências do frontend usando o npm:
```bash
npm install
```

3.2. Rodando o Frontend em Desenvolvimento
Para rodar o frontend em modo de desenvolvimento, execute:
```bash
npm start
```
Isso vai iniciar o servidor de desenvolvimento do React, geralmente na URL http://localhost:3000/.

3.3. Criando o Build de Produção
Caso queira gerar uma versão otimizada para produção, use o seguinte comando:
```bash
npm run build
```
Esse comando cria a versão otimizada do seu aplicativo React na pasta build. O Flask pode servir esse build na produção.

4. Integração Backend-Frontend
No backend, a aplicação Flask serve o frontend React. Quando você executar o backend com python run.py, ele irá automaticamente servir a versão de produção do frontend, se você já tiver rodado o build do React. Caso contrário, ele serve a aplicação diretamente no modo de desenvolvimento.

5. Verificando a API
O Flask fornece uma API RESTful para a comunicação com o frontend. Para testar a comunicação com a API, você pode usar o Postman ou qualquer outra ferramenta para fazer requisições HTTP para a URL http://127.0.0.1:5000/. Algumas rotas de exemplo podem ser:

POST /auth/login: Realiza login no sistema.
GET /tasks: Obtém a lista de tarefas.
POST /tasks: Cria uma nova tarefa.

6. Estrutura do Projeto
```arduino
projeto-tasksync/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── templates/
│   ├── utils/
│   ├── extensions.py
│   ├── frontend/                  # Frontend React
│   │   ├── package.json
│   │   ├── src/
│   │   │   ├── main.jsx
│   │   │   ├── App.jsx
│   │   │   ├── api/
│   │   │   ├── components/
│   │   │   ├── pages/
│   │   │   ├── styles/
│   │   │   └── utils/
│   │   ├── public/
│   │   ├── .gitignore
│   │   ├── vite.config.js
│   │   ├── README.md
│   │   ├── .env
│   │   └── package-lock.json
│
├── migrations/
│
├── requirements.txt
├── .env
├── .gitignore
├── run.py
└── README.md
```
