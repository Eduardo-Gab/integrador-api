from fastapi import FastAPI
from models import Session, Cotacao

app = FastAPI(title="API de Cotacoes")

@app.get("/cotacoes")
def listar_cotacoes():
    session = Session()
    resultado = session.query(Cotacao).order_by(Cotacao.data_atualizacao.desc()).limit(20).all()
    session.close()
    return [{"moeda": c.moeda, "valor": c.valor, "data": c.data_atualizacao} for c in resultado]

@app.get("/cotacoes/{moeda}")
def cotacao_por_moeda(moeda: str):
    session = Session()
    resultado = session.query(Cotacao).filter(Cotacao.moeda == moeda.upper()).order_by(Cotacao.data_atualizacao.desc()).first()
    session.close()
    if resultado:
        return {"moeda": resultado.moeda, "valor": resultado.valor}
    return {"erro": "Moeda nao encontrada"}
