Cliente
  nome
  sobrenome
  cpf
  Endereco
    cep
    rua
    numero
    complemento
    bairro
    cidade
    estado
  Contato
    telefone
    whatsapp
    email

Carro
modelo
motor
ano
versao
km
combustivel =  ['Alcool','Gasolina','Flex']
cor
portas =  ['2 portas','4 portas']
  
  OleoMotor
    idCarro
    espeficicao
    capacidade
    bujao
    filtroOleo
    
  Arrefecimento
    idCarro
    capacidade
  
  TabelaFipe
    idCarro
    preco
    
  
  Defeito
    Produto
    Servico
    
    
Orcamento
Oficina
AutoPecas
Anuncio
  idCliente
  idCarro
  Detalhes
    Carro.Ano
    Carro.Km
    Carro.combustivel
    AceitoTroca =True or False
    Carro.cor
    Carro.porta
    
  Acessorios
  Observacoes
  
  
