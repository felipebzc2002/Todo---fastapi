# 🚀 FastAPI Zero

> API de gestão de usuários e tarefas com autenticação JWT, PostgreSQL e containerização, desenvolvida como projeto acadêmico para compor meu portfólio em backend.

[![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Poetry](https://img.shields.io/badge/Poetry-2.0-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org/)
[![License](https://img.shields.io/badge/License-Personal%20Use-8A2BE2?style=for-the-badge)](LICENSE)

---

## 📌 Sobre o Projeto

O FastAPI Zero é uma API REST para gerenciamento de usuários e tarefas, desenvolvida como um projeto pessoal acadêmico com foco em backend, autenticação, persistência em banco de dados relacional e boas práticas de engenharia de software.

A aplicação foi construída para demonstrar conhecimentos em:

- criação de APIs REST com FastAPI;
- autenticação e autorização baseada em JWT;
- modelagem de entidades com SQLAlchemy e PostgreSQL;
- versionamento de banco com Alembic;
- uso de Docker para isolamento de ambiente e reprodução consistente;
- escrita de testes automatizados com Pytest;
- organização modular por routers, schemas, models e settings.

> Este projeto foi pensado para servir como referência prática, demonstrando capacidade de estruturar aplicações do mundo real com foco em qualidade, segurança e manutenção.

---

## 🛠️ Tech Stack

| Categoria | Tecnologias |
|---|---|
| Linguagem | Python 3.13 |
| Framework API | FastAPI |
| Banco de Dados | PostgreSQL |
| ORM / acesso assíncrono | SQLAlchemy AsyncIO |
| Migrações | Alembic |
| Autenticação | JWT + OAuth2 Password Bearer |
| Gerenciamento de dependências | Poetry |
| Testes | Pytest + pytest-cov |
| Containerização | Docker + Docker Compose |
| Segurança | Argon2 + Password hashing |

### 🔐 Configurações reais do projeto

O projeto usa as variáveis abaixo definidas em `fastapi_zero/settings.py`:

```python
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
```

Essas configurações são carregadas a partir do arquivo `.env` pela biblioteca `pydantic-settings`.

---

## ✨ Funcionalidades

### ✅ Autenticação e segurança

- Login com email e senha em `POST /auth/token`;
- renovação de token em `POST /auth/refresh_token`;
- proteção de rotas privadas via `Depends(current_user)`;
- hash de senha com `pwdlib[argon2]`;
- autenticação via JWT com `Bearer Token`.

### 👤 Gestão de usuários

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/users/` | Criação de novo usuário |
| `GET` | `/users/` | Listagem de usuários com paginação (`limit`, `offset`) |
| `PUT` | `/users/{user_id}` | Atualização de dados do próprio usuário |
| `DELETE` | `/users/{user_id}` | Exclusão do próprio usuário |

### ✅ Gestão de tarefas

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/todos/` | Criação de uma tarefa |
| `GET` | `/todos/` | Listagem de tarefas do usuário autenticado |
| `PATCH` | `/todos/{todo_id}` | Atualização parcial da tarefa |
| `DELETE` | `/todos/{todo_id}` | Remoção da tarefa |

### 🗂️ Entidades e status

Os modelos reais do projeto são:

- `User`
  - `id`
  - `username`
  - `email`
  - `password`
  - `created_at`

- `Todo`
  - `id`
  - `nome`
  - `descricao`
  - `user_id`
  - `status`

O status da tarefa usa o enum `TodoState` com os valores:

```python
class TodoState(str, Enum):
    draft = 'draft'
    todo = 'todo'
    doing = 'doing'
    done = 'done'
    trash = 'trash'
```

### 🧩 Recursos adicionais

- paginação básica com `limit` e `offset`;
- filtros por título e descrição em tarefas;
- isolamento de ambiente com Docker;
- migrações automáticas via Alembic antes do startup da aplicação;
- estrutura modular e reutilizável para evoluir para novas features.

---

## 📁 Estrutura de Pastas

```text
fastapi_zero/
├── alembic.ini
├── compose.yaml
├── Dockerfile
├── entrypoint.sh
├── pyproject.toml
├── README.md
├── fastapi_zero/
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   ├── settings.py
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       ├── todos.py
│       └── users.py
├── migrations/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       ├── bc45e632fcd0_create_users_table.py
│       └── d763886e1d49_criar_tabela_de_todos.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_app.py
│   └── test_db.py
├── htmlcov/
│   └── relatórios de cobertura gerados pelo pytest
└── .env
```

### 📦 O que cada módulo faz

- `routers/`: expõe os endpoints agrupados por domínio (`auth`, `users`, `todos`);
- `models.py`: define as tabelas e relacionamentos do SQLAlchemy;
- `schemas.py`: valida e serializa os payloads de entrada e saída da API;
- `migrations/`: versiona o banco de dados com Alembic;
- `security.py`: lógica de hash e autenticação JWT;
- `database.py`: conexão assíncrona com PostgreSQL.

---

## 🚀 Como Executar o Projeto

### ✅ Pré-requisitos

- Git
- Docker e Docker Compose instalados
- Python 3.13 + Poetry

### 1) Clone o projeto

```bash
git clone <url-do-repositorio>
cd fastapi_zero
```

### 2) Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no seguinte conteúdo:

```env
DATABASE_URL=postgresql+asyncpg://app_user:app_password@localhost:5432/app_db
SECRET_KEY=sua-chave-secreta-muito-forte
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

> Se você estiver rodando com Docker Compose, o container do banco recebe automaticamente o valor `DATABASE_URL=postgresql+asyncpg://app_user:app_password@fastzero_database:5432/app_db` no ambiente da aplicação.

### 3) Instale as dependências

```bash
poetry install
```

### 4) Suba o ambiente com Docker Compose

```bash
docker compose up --build
```

Esse comando inicia:

- o serviço PostgreSQL em `fastzero_database`;
- a API FastAPI em `fastapi_app`;
- a aplicação com o `entrypoint.sh`.

### 5) Migrações automáticas

O script de entrada do projeto executa as migrações do Alembic antes de iniciar o servidor:

```sh
#!/bin/sh
poetry run alembic upgrade head
poetry run uvicorn --host 0.0.0.0 --port 8000 fastapi_zero.app:app
```

Isso garante que o schema do banco esteja atualizado automaticamente no boot da aplicação.

### 6) Execução local sem Docker

```bash
poetry run fastapi dev fastapi_zero/app.py
```

A API ficará disponível em:

```text
http://localhost:8000
```

---

## 📖 Documentação Interativa

Após subir o projeto, você pode acessar:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

A interface Swagger permite testar os endpoints diretamente na própria documentação, incluindo autenticação e envio de payloads JSON.

---

## 🧪 Testes

O projeto utiliza `pytest` para validar o comportamento da API.

### ▶️ Rodar testes localmente

```bash
poetry run pytest
```

### ▶️ Rodar com cobertura

```bash
poetry run pytest --cov=fastapi_zero
```

### ▶️ Rodar com Taskipy

O `pyproject.toml` define tarefas de desenvolvimento, incluindo lint e execução de testes:

```bash
poetry run task test
poetry run task lint
````

### ✅ Observação

Os testes existentes validam a criação e leitura de usuários e a resposta da rota raiz da aplicação. O projeto também já está preparado para evoluir para testes de autenticação, tarefas e fluxo completo de autorização.

---

## 🧭 Endpoints da API

### Autenticação

```http
POST /auth/token
POST /auth/refresh_token
```

### Usuários

```http
POST /users/
GET /users/
PUT /users/{user_id}
DELETE /users/{user_id}
```

### Tarefas

```http
POST /todos/
GET /todos/
PATCH /todos/{todo_id}
DELETE /todos/{todo_id}
```

---

## 👨‍💻 Autor

Olá! Sou Felipe Carvalho, estudante de Engenharia de Software, com grande interesse em backend, arquitetura de sistemas, APIs REST, infraestrutura e desenvolvimento de software escalável.

Este projeto representa uma etapa importante da minha jornada acadêmica e profissional, consolidando conceitos de:

- desenvolvimento de serviços web robustos;
- integração com bancos relacionais;
- autenticação e segurança;
- produção de projetos com qualidade e clareza de código;
- documentação técnica para portfólio e apresentação profissional.

### Conecte-se comigo

- GitHub: [github.com/seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [linkedin.com/in/seu-perfil](https://linkedin.com/in/seu-perfil)
- Email: felipebzc1101@gmail.com

---

## 🏁 Conclusão

Este projeto foi estruturado para demonstrar uma base sólida de desenvolvimento backend com Python e FastAPI, combinando práticas modernas de engenharia com foco em qualidade, organização e portabilidade.

Ele é uma ótima referência para quem deseja evoluir em:

- APIs assíncronas com FastAPI;
- autenticação JWT;
- design de modelos e schemas;
- uso de Docker em projetos Python;
- migrações de banco com Alembic;
- documentação e testes como parte do ciclo de desenvolvimento.

Se você quiser, também posso criar uma segunda versão deste README com foco em apresentação de portfólio, incluindo screenshots, badges mais premium e uma seção de resultados/arquitetura de software.
