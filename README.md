# Integrador de Cotacoes via API

Integrador que consome a API publica AwesomeAPI (cotacao de moedas), salva os dados em SQLite com SQLAlchemy, sincroniza a cada 10 minutos com schedule e expoe tudo por uma API propria feita com FastAPI.

## Como rodar

    pip install -r requirements.txt
    python sincronizador.py

Em outro terminal, suba a API:

    uvicorn api:app --reload

A documentacao interativa fica em http://127.0.0.1:8000/docs
