Cliente
  idCliente
  nome
  sobrenome
  cpf
  
  
  
 Endereco
    idCliente
    cep
    rua
    numero
    complemento
    bairro
    cidade
    estado
    
Contato
    idCliente
    telefone
    whatsapp
    email

Carro
  modelo = varchar
  motor = varchar
  ano = int
  versao = varchar
  km = int
  combustivel =  ['Alcool','Gasolina','Flex']
  cor = varchar
  portas =  ['2 portas','4 portas']

Cliente_Carro1:
  idCarro
  idCliente
  
  
OleoMotor
  idOleoMotor
  idCarro
  OleoMotorProduto = FKidProduto ['oleo']
  capacidade = varchar
  bujao = FKidProduto ['Bujao']
  filtroOleo = FKidProduto ['Filtro de Oleo']
 
Arrefecimento
  idArrefecimento
  idCarro
  capacidadeSistema = varchar
  
  

TabelaFipe
  idCarro
  preco
    
  
Defeito
  idCliente
  DefeitoTitulo
  
  
    
    
Produto
  idProduto
  ProdutoDescricao
  ProdutoCodigo
  ProdutoPreco
  ProdutoEstoque
  ProdutoAplicacao
  

Servico
  idServico
  idCarro
  ServicoTitulo
  ServicoPreco
  ServicoTempoExecucao
  idProduto=Manytomany
  
  
ClienteOficina
  idCliente
  idOficina
  
Oficina
  idClienteOficina
  OficinaNome
  OficinaTelefone
  OficinaRating

  
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
  
  
