#gerenciador de tarefas

# adicionar tarefa com um nome e uma descrição
# listar todas as tarefas
#marcar uma tarefa como concluída
#remover uma tarefa

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import secrets

app = FastAPI()

MEU_USUARIO = "admin"
MINHA_SENHA = "senha123"

security = HTTPBasic()

tarefas = {}

class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: Optional[bool] = False
    
def autenticar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, MEU_USUARIO)
    correct_password = secrets.compare_digest(credentials.password, MINHA_SENHA)
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Usuário ou senha incorretos", headers={"WWW-Authenticate": "Basic"})
    return credentials.username

@app.get("/listar_tarefas")
def listar_tarefas(page: int = 1, size: int = 10, order_by: str = "nome", credenciais: HTTPBasicCredentials = Depends(autenticar_usuario)):
    if page < 1 or size < 1:
        raise HTTPException(status_code=400, detail="Parâmetros de paginação inválidos")
    if not tarefas:
        raise HTTPException(status_code=404, detail="Nenhuma tarefa encontrada")
    
    tarefas_ordenadas = sorted(tarefas.values(), key=lambda x: getattr(x, order_by))

    start = (page - 1) * size
    end = start + size
    tarefas_paginadas = [
        {"nome": tarefa.nome,
         "descricao": tarefa.descricao,
         "concluida": tarefa.concluida}
        for tarefa in tarefas_ordenadas[start:end]
    ]
    return {
        "page": page,
        "size": size,
        "total": len(tarefas),
        "tarefas": tarefas_paginadas,
    }

@app.post("/adicionar_tarefas")
def adicionar_tarefa(tarefa: Tarefa, credenciais: HTTPBasicCredentials = Depends(autenticar_usuario)):
    if tarefa.nome in tarefas:
        raise HTTPException(status_code=400, detail="Tarefa já existe")
    tarefas[tarefa.nome] = tarefa
    return {"message": "Tarefa adicionada com sucesso"}


@app.put("/marcar_concluida/{nome}")
def marcar_concluida(nome: str, credenciais: HTTPBasicCredentials = Depends(autenticar_usuario)):
    if nome not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefas[nome].concluida = True
    return {"message": "Tarefa marcada como concluída"}

@app.delete("/remover_tarefa/{nome}")
def remover_tarefa(nome: str, credenciais: HTTPBasicCredentials = Depends(autenticar_usuario)):
    if nome not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    del tarefas[nome]
    return {"message": "Tarefa removida com sucesso"}