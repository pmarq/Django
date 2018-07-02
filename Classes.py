Cliente
  idCliente
  nome
  sobrenome
  cpf
  
  
  
 Cliente_Endereco
    idCliente
    cep
    rua
    numero
    complemento
    bairro
    cidade
    estado
    
Cliente_Contato
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
  
Cliente_Carro2:
  idCarro
  idCliente  
  
CarroOleoMotor
  idOleoMotor
  idCarro
  OleoMotorProduto = FKidProduto ['oleo']
  capacidade = varchar
  bujao = FKidProduto ['Bujao']
  filtroOleo = FKidProduto ['Filtro de Oleo']
 
CarroArrefecimento
  idArrefecimento
  idCarro
  capacidadeSistema = varchar
  
  

CarroTabelaFipe
  idCarro
  preco
    
  
CarroDefeito 
  idCarro
  idServico
  idProduto
  DefeitoTitulo
  
#Exemplo de um defeito:
#Carro: Fox 1.0 8v Flex
#Defeito: Vazamento de oleo no motor

#Produtos a serem conferidos:
  #Tampa de valvula
    #ServiçoTitulo: Troca do sistema     
  
  #Interruptor de pressão do Oleo
  
  #AntiChama
  
    #ServiçoTitulo: Troca do sistema de anti-chamas
    #ServicoProdutos: ['AntiChama-CWB1536']
    #ServicoMenorPreco:[60,00]
    #ServicoMaiorPreco: [90,00]
  
  #Carter

#Serviço:
#
#
  
    
    
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
  
  
//////////////////////////////////////////////////////  

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
  
  
