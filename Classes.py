

class Carro(object):

    def __init__(self,CodeCar,Montadora,DescComp,
                 DescReduz,AnoIni,AnoFim,NomeCarro,
                 MotorCarro,ModeloCarro,DadosMotor):
        self.idVeiculo = None
        self.CodeCar = CodeCar
        self.Montadora = Montadora
        self.DescricaoCompleta = DescComp
        self.DescricaoReduzida = DescReduz
        self.AnoInicial = AnoIni
        self.AnoFinal = AnoFim
        self.NomeCarro = NomeCarro
        self.MotorCarro = MotorCarro
        self.ModeloCarro = ModeloCarro
        self.DadosMotor = DadosMotor

    pass


class Aplicacao():

    def __init__(self,NomePeca,Produto1,
                 Produto2,Produto3,idVeiculo):
        self.idApplycar = None
        self.NomePeca = NomePeca
        self.ID_Produto1 = Produto1
        self.ID_Produto2 = Produto2
        self.ID_Produto3 = Produto3
        self.ID_Veiculo = idVeiculo



class Produto():

    def __init__(self,CodProd,NomeProd,Fabricante,
                 Quantidade,Localz,Excluir,PrecoCusto):

        self.CodigoProduto = CodProd
        self.NomeProduto = NomeProd
        self.Fabricante = Fabricante
        self.Quantidade = Quantidade
        self.Localizacao = Localz
        self.Excluir = Excluir
        self.PrecoCusto = PrecoCusto
        self.idProduto = None




