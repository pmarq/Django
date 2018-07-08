

class Montadora(models.Model):
    nome = models.CharField(max_length=80)
    def __str__(self):
        return self.nome

class Carro(models.Model):
    modelo = models.CharField(max_length=120)
    motor = models.CharField(max_length=50)
    ano = models.IntegerField
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo + " " + self.motor + " " + self.ano
    pass

class Cliente(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField
    telefone = models.CharField(max_length=15)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome + " " + self.carro
    pass


class Fabricante(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome
    pass


class Peca(models.Model):
    descricao = models.CharField(max_length=120)
    codigo = models.CharField(max_length=30)
    fabricante = models.OneToOneField(Fabricante, on_delete=models.CASCADE)
    Preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.descricao + " " + self.codigo + " - " +self.fabricante
    pass


class Pivo(models.Model):

    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    lado = models.CharField(max_length=20)


class TerminalDirecao(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    lado = models.CharField(max_length=20)

class ArticulacaoAxial(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    lado = models.CharField(max_length=20)

class AmortDt(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    lado = models.CharField(max_length=20)

class AmortTras(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    lado = models.CharField(max_length=20)

class kitAmortDt(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    lado = models.CharField(max_length=20)

class kitAmortTras(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    lado = models.CharField(max_length=20)

class SuspensaoCarro(models.Model):

    car = models.ForeignKey(Carro, on_delete=models.CASCADE)
    pivo = models.ForeignKey(Pivo, on_delete=models.CASCADE)
    terminal = models.ForeignKey(TerminalDirecao, on_delete=models.CASCADE)
    axial = models.ForeignKey(ArticulacaoAxial, on_delete=models.CASCADE)
    amortecedor_dt = models.ForeignKey(AmortDt, on_delete=models.CASCADE)
    amortecedor_tras = models.ForeignKey(AmortTras, on_delete=models.CASCADE)
    kit_amort_dt = models.ForeignKey(kitAmortDt, on_delete=models.CASCADE)
    kit_amort_tras = models.ForeignKey(kitAmortTras, on_delete=models.CASCADE)

    def __str__(self):
        return self.car + " Peças para suspensão ."

