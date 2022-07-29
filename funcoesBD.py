from cmath import nan
from ModeloDB import Telefones,db_session


def consulta():
    telefones = Telefones.query.filter(Telefones.valido == None).first()
    id = {telefones.id}
    fone = f'({telefones.ddd}{telefones.fone})'
    valido = {telefones.valido}
    telefone = (fone[1:-1])
    return telefone


def insert(ddd,fone):
    telefones = Telefones(ddd=ddd,fone=fone)
    telefones.save()
    print('Inserido os dados com sucesso')

def update(telefone,status):
    telefones = Telefones.query.filter_by(ddd = telefone[0:2],fone = telefone[2:]).first()
    telefones.valido = status
    telefones.save()

def consultatotal():
    telefones = Telefones.query.all()
    for t in telefones:
        print(t.id,t.ddd,t.fone,t.valido)




if __name__ == '__main__':
    #insert()
    #print(consulta())
    #update('11986828520',1)
    consultatotal()
