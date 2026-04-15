#  API de Tarefas com FastAPI

Este é um **mini projeto de backend em Python** utilizando **FastAPI**, desenvolvido com foco em **aprendizado**, **boas práticas** e **conceitos fundamentais de API REST**.

O projeto implementa um **CRUD completo** (Create, Read, Update e Delete) usando um banco de dados em memória, sendo ideal para quem está começando no desenvolvimento backend com Python.

 **Projeto desenvolvido ao vivo durante uma live no canal _Desvendando o Código_, com explicação passo a passo e foco didático.**

# Link da live https://youtube.com/live/c4bCbxPQ23c
---

##  Tecnologias utilizadas

- Python 3
- FastAPI
- Pydantic
- Uvicorn

---

##  Funcionalidades

- Listar todas as tarefas
- Criar uma nova tarefa
- Buscar tarefa por ID
- Atualizar tarefa existente
- Remover tarefa
- Tratamento de erro (404 – tarefa não encontrada)
- Documentação automática com Swagger

---

##  Rotas da API

| Método | Rota          | Descrição                |
|--------|---------------|--------------------------|
| GET    | /tarefas      | Lista todas as tarefas   |
| POST   | /tarefas      | Cria uma nova tarefa     |
| GET    | /tarefas/{id} | Busca uma tarefa pelo ID |
| PUT    | /tarefas/{id} | Atualiza uma tarefa      |
| DELETE | /tarefas/{id} | Remove uma tarefa        |

---

##  Documentação (Swagger)

Após executar o projeto, a documentação interativa da API estará disponível em:

## http://localhost:8000/docs

## uvicorn main:app --reload

