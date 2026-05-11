#gerenciador de tarefas

# adicionar tarefa com um nome e uma descrição
# listar todas as tarefas
#marcar uma tarefa como concluída
#remover uma tarefa

from fastapi import FastAPI, HTTPException

app = FastAPI()
tarefas = {}

@app.post("/adicionar_tarefas")
def adicionar_tarefa(nome: str, descricao: str):
    if nome in tarefas:
        raise HTTPException(status_code=400, detail="Tarefa já existe")
    tarefas[nome] = {"descricao": descricao, "concluida": False}
    return {"message": "Tarefa adicionada com sucesso"}

@app.get("/listar_tarefas")
def listar_tarefas():
    return {"tarefas": tarefas}

@app.put("/marcar_concluida/{nome}")
def marcar_concluida(nome: str):
    if nome not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefas[nome]["concluida"] = True
    return {"message": "Tarefa marcada como concluída"}

@app.delete("/remover_tarefa/{nome}")
def remover_tarefa(nome: str):
    if nome not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    del tarefas[nome]
    return {"message": "Tarefa removida com sucesso"}