from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class Cotacao(Base):
    __tablename__ = 'cotacoes'
    id = Column(Integer, primary_key=True)
    moeda = Column(String)
    valor = Column(Float)
    data_atualizacao = Column(DateTime, default=datetime.now)

engine = create_engine('sqlite:///database/cotacoes.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
