import sqlite3
conexao = sqlite3.connect('ITAU')
cursor = conexao.cursor()


class ProdutoOut:
    def __init__(self):
        self.a = []
        self.b = []
        self.c = []
        self.d = []



Pout = ProdutoOut()

Pout.aOut = cursor.execute('''create table CarroOut(nome text)''')
Pout.bOut = cursor.execute('''create table MotorOut(nome text)''')
Pout.cOut = cursor.execute('''create table AnoOut(nome text)''')
Pout.dOut = cursor.execute('''create table StarOut (nome text)''')

class ProdutoIn:
    def __init__(self):
        self.a = []
        self.b = []
        self.c = []
        self.d = []



pIN = ProdutoIn()

pIN.aiN = cursor.execute('''create table CarroIn(nome text)''')
pIN.biN = cursor.execute('''create table MotorIn(nome text)''')
pIN.ciN = cursor.execute('''create table AnoIn(nome text)''')
pIN.diN = cursor.execute('''create table StarIn (nome text)''')








conexao.commit()
cursor.close()


