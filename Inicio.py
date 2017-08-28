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



class Carro:
    def __init__(self):
        self.c1 = ARGO
        self.c2 = CINQUECENTO
        self.c3 = BRAVA
        self.c4 = BRAVO
        self.c5 = COUPÉ
        self.c6 = DOBLÒ
        self.c7 = DUCATO
        self.c8 = ELBA
        self.c9 = FIORINO
        self.c10 = FREEMONT
        self.c11 = IDEA
        self.c12 = LINEA
        self.c13 = MAREA
        self.c14 = PALIO
        self.c15 = PRÊMIO
        self.c16 = PUNTO
        self.c17 = SIENA
        self.c18 = STILO
        self.c19 = STRADA
        self.c20 = TEMPRA
        self.c21 = TIPO
        self.c22 = UNO
        self.c23 = TORO
        self.c24 = MOBI


car = Carro()

car.c1 = True



#motores
class Motores:
    def __init__(self):
        self.M1	= 1.0
        self.M2 = 1.1
        self.M3 = 1.2
        self.M4 = 1.3
        self.M5 = 1.4
        self.M6 = 1.5
        self.M7 = 1.6
        self.M8 = 1.7
        self.M9 = 1.8
        self.M10 = 1.9
        self.M11 = 2.0
        self.M12 = 2.2
        self.M13 = 2.3
        self.M14 = 2.4
        self.M15 = 2.5
        self.M16 = 2.6
        self.M17 = 2.7
        self.M18 = 2.8
        self.M19 = 2.9
        self.M20 = 3.0
        self.M21 = 3.1

class Ano:
    def __init__(self):
        self.A1 = 1975
        self.A2 = 1976
        self.A3 = 1977
        self.A4 = 1978
        self.A5 = 1979
        self.A6 = 1980
        self.A7 = 1981
        self.A8 = 1982
        self.A9 = 1983
        self.A10 = 1984
        self.A11 = 1985
        self.A12 = 1986
        self.A13 = 1987
        self.A14 = 1988
        self.A15 = 1989
        self.A16 = 1990
        self.A17 = 1991
        self.A18 = 1992
        self.A19 = 1993
        self.A20 = 1994
        self.A21 = 1995
        self.A22 = 1996
        self.A23 = 1997
        self.A24 = 1998
        self.A25 = 1999
        self.A26 = 2000
        self.A27 = 2001
        self.A28 = 2002
        self.A29 = 2003
        self.A30 = 2004
        self.A31 = 2005
        self.A32 = 2006
        self.A33 = 2007
        self.A34 = 2008
        self.A35 = 2009
        self.A36 = 2010
        self.A37 = 2011
        self.A38 = 2012
        self.A39 = 2013
        self.A40 = 2014
        self.A41 = 2015
        self.A42 = 2016
        self.A43 = 2017
        self.A44 = 2018
        self.A45 = 2019



class Produto:
    def __init__(self):
        self.P3 = "  Coifa da alavanca de câmbio    "
        self.P4 = "  Descansa braço "
        self.P5 = "  Manopla do câmbio  "
        self.P6 = "  Quebra-sol "
        self.P7 = "  Tampão do porta-malas  "
        self.P10 = "  Calha de chuva "
        self.P11 = "  Capa de carro  "
        self.P12 = "  Protetor do cárter "
        self.P13 = "  Rack transversal   "
        self.P14 = "  Spoiler lateral    "
        self.P15 = "  Amortecedor dianteiro  "
        self.P16 = "  Amortecedor do porta-malas "
        self.P17 = "  Amortecedor traseiro   "
        self.P18 = "  Kit do amortecedor dianteiro   "
        self.P21 = "  Borracha da porta  "
        self.P22 = "  Canaleta   "
        self.P25 = "  Chave de seta  "
        self.P26 = "  Interruptor do vidro   "
        self.P27 = "  Soquete da lanterna traseira   "
        self.P28 = "  Disco de freio "
        self.P29 = "  Pastilha de freio  "
        self.P30 = "  Friso do teto  "
        self.P31 = "  Friso lateral  "
        self.P32 = "  Cabo de vela   "
        self.P33 = "  Vela de ignição    "
        self.P34 = "  Farol  "
        self.P35 = "  Farol de milha "
        self.P36 = "  Kit de farol de milha  "
        self.P37 = "  Kit lâmpada do farol   "
        self.P38 = "  Lanterna dianteira "
        self.P39 = "  Lanterna traseira  "
        self.P40 = "  Cinto de segurança "
        self.P41 = "  Assoalho   "
        self.P42 = "  Capô dianteiro "
        self.P43 = "  Para-lama dianteiro    "
        self.P44 = "  Fechadura da porta "
        self.P45 = "  Maçaneta externa da porta  "
        self.P46 = "  Maçaneta interna da porta  "
        self.P47 = "  Máquina de vidro   "
        self.P50 = "  Entrada de ar do painel    "
        self.P51 = "  Grade do para-choque   "
        self.P52 = "  Para-choque dianteiro  "
        self.P53 = "  Para-choque traseiro   "
        self.P54 = "  Capa do retrovisor "
        self.P55 = "  Lente do retrovisor com base   "
        self.P56 = "  Lente do retrovisor sem base   "
        self.P57 = "  Retrovisor externo "
        self.P58 = "  Revestimento de porta  "
        self.P59 = "  Tapete de borracha "
        self.P60 = "  Limpador do para-brisa "

orcamento =
venda =
