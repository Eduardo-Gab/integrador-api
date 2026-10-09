import requests
import schedule
import time
from models import Session, Cotacao

def sincronizar():
    try:
        resp = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
        dados = resp.json()
        
        session = Session()
        for chave, info in dados.items():
            cotacao = Cotacao(moeda=info['code'], valor=float(info['bid']))
            session.add(cotacao)
        session.commit()
        session.close()
        print(f"Sincronizado com sucesso: {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Erro na sincronizacao: {e}")

if __name__ == '__main__':
    sincronizar()
    schedule.every(10).minutes.do(sincronizar)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
