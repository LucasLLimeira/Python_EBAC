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

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./tarefas.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

MEU_USUARIO = "admin"
MINHA_SENHA = "senha123"

security = HTTPBasic()

class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: Optional[bool] = False

class TarefaDB(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    descricao = Column(String)
    concluida = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
def autenticar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, MEU_USUARIO)
    correct_password = secrets.compare_digest(credentials.password, MINHA_SENHA)
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Usuário ou senha incorretos", headers={"WWW-Authenticate": "Basic"})
    return credentials.username

@app.get("/listar_tarefas")
def listar_tarefas(page: int = 1, size: int = 10, order_by: str = "nome", db: Session = Depends(get_db), credenciais: HTTPBasicCredentials = Depends(autenticar_usuario)):
    if page < 1 or size < 1:
        raise HTTPException(status_code=400, detail="Parâmetros de paginação inválidos")
    campos_validos = {"id", "nome", "descricao", "concluida"}
    if order_by not in campos_validos:
        raise HTTPException(status_code=400, detail=f"Campo de ordenação inválido. Use um dos seguintes: {', '.join(sorted(campos_validos))}")
    
    tarefas_base_query = db.query(TarefaDB).order_by(getattr(TarefaDB, order_by))
    total = tarefas_base_query.count()

    if total == 0:
        raise HTTPException(status_code=404, detail="Nenhuma tarefa encontrada")
    
    tarefas_ordenadas = tarefas_base_query.offset((page - 1) * size).limit(size).all()

    return {
        "page": page,
        "size": size,
        "total": total,
        "tarefas": [{"id": tarefa.id, "nome": tarefa.nome, "descricao": tarefa.descricao, "concluida": tarefa.concluida} for tarefa in tarefas_ordenadas],
    }

@app.post("/adicionar_tarefas")
def adicionar_tarefa(tarefa: Tarefa, db: Session = Depends(get_db), credenciais: HTTPBasicCredentials = Depends(autenticar_usuario)):
    if db.query(TarefaDB).filter(TarefaDB.nome == tarefa.nome).first():
        raise HTTPException(status_code=400, detail="Tarefa com esse nome já existe")
    tarefa_db = TarefaDB(nome=tarefa.nome, descricao=tarefa.descricao, concluida=tarefa.concluida)
    db.add(tarefa_db)
    db.commit()
    db.refresh(tarefa_db)
    return {"message": f"Tarefa {tarefa_db.nome} adicionada com sucesso", "id": tarefa_db.id}


@app.put("/marcar_concluida/{nome}")
def marcar_concluida(nome: str, db: Session = Depends(get_db), credenciais: HTTPBasicCredentials = Depends(autenticar_usuario)):
    tarefa_db = db.query(TarefaDB).filter(TarefaDB.nome == nome).first()
    if not tarefa_db:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa_db.concluida = True
    db.commit()
    db.refresh(tarefa_db)
    return {"message": f"Tarefa {tarefa_db.nome} marcada como concluída", "id": tarefa_db.id}

@app.delete("/remover_tarefa/{nome}")
def remover_tarefa(nome: str, db: Session = Depends(get_db), credenciais: HTTPBasicCredentials = Depends(autenticar_usuario)):
    tarefa_db = db.query(TarefaDB).filter(TarefaDB.nome == nome).first()
    if not tarefa_db:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(tarefa_db)
    db.commit()
    return {"message": f"Tarefa {tarefa_db.nome} removida com sucesso", "id": tarefa_db.id}