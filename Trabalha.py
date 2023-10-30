import json
from urllib import response
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Locacao(BaseModel):
    id: int
    nome: str
    data_locacao: str

locacoes_db = []

@app.post("/locacoes", response_model=Locacao)
def create_locacao(locacao: Locacao):
    locacoes_db.append(locacao)
    return locacao

@app.get("/locacoes", response_model=List[Locacao])
def get_locacoes():
    return locacoes_db

@app.delete("/locacoes/{locacao_id}", status_code=204)
def excluir_locacao(locacao_id: int):
    for registro in locacoes_db:
          
        if (locacoes_db.get("id") == id):
            registro_existe = registro
            break

    # Se existir um registro, vai retornar uma mensagem
    if (not registro_existe):
        content = json.dumps({"mensagem": "Nao ha registro "})
        return response(content=content,
                        status_code=404,
                        media_type="application/json")
    
    locacoes_db.remove(registro_existe)

    locacoes_db(content=None,
             status_code=203,
             media_type="application/json")
   