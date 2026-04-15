# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


#CRIANDO A INSTÂNCIA DO FASTAPI
app = FastAPI(title="API de Tarefas")

#DEFININDO O MODELO DE DADOS PARA AS TAREFAS
class Tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluida: bool = False
#SIMULANDO UM BANCO DE DADOS EM MEMÓRIA
db_tarefas = []

#ROTA PARA LISTAR TODAS AS TAREFAS
@app.get('/tarefas', response_model=List[Tarefa])
async def listar_tarefas():
    return db_tarefas

#ROTA PARA CRIAR UMA NOVA TAREFA
@app.post('/tarefas', response_model=Tarefa)
async def criar_tarefa(tarefa: Tarefa):
    #Atribuindo um ID único para a nova tarefa
    tarefa.id = len(db_tarefas) + 1
    #Adicionando a tarefa ao "banco de dados"
    db_tarefas.append(tarefa)
    #Retornando a tarefa criada
    return tarefa

#ROTA PARA BUSCAR TAREFA POR ID
@app.get('/tarefas/{tarefa_id}', response_model=Tarefa)
async def buscar_tarefa(tarefa_id: int):
    for tarefa in db_tarefas:
        if tarefa.id == tarefa_id:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")        

#ROTA PARA ATUALIZAR UMA TAREFA
@app.put('/tarefas/{tarefa_id}', response_model=Tarefa)
async def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa):
    for index, tarefa in enumerate(db_tarefas):
        if tarefa.id == tarefa_id:
            db_tarefas[index] = tarefa_atualizada
            db_tarefas[index].id = tarefa_id  # Garantir que o ID permaneça o mesmo
            return db_tarefas[index]
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

#ROTA PARA DELETAR UMA TAREFA
@app.delete('/tarefas/{tarefa_id}')
async def deletar_tarefa(tarefa_id: int):
    for index, tarefa in enumerate(db_tarefas):
        if tarefa.id == tarefa_id:
            del db_tarefas[index]
            return {"detail": "Tarefa deletada com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")    
