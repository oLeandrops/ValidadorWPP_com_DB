from sqlalchemy import Column, create_engine,Integer,String
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#CRIAÇÃO DO BANCO DE DADOS
engine = create_engine('sqlite:///basetelefones.db', convert_unicode = True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                        bind=engine))


base = declarative_base()
base.query = db_session.query_property()

#CRIAÇÃO DA TABELA

class Telefones(base):
    __tablename__= 'telefones'
    id = Column(Integer, primary_key = True)
    ddd = Column(String(2))
    fone = Column(String(11), index = True)
    valido = Column(Integer)

    def __repr__(self):
        return f'{self.ddd}{self.fone}'
        

    def save(self):
        db_session.add(self)
        db_session.commit()


#CRIACAO EFETIVA PARA CRIAR O BANCO
def init_db():
    base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()

