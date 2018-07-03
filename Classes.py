#<Login>

Cliente
  idCliente PK, AI, NN
  ClienteNome
  ClienteSobrenome
  ClienteCpf
  ClienteLogin
  ClienteSenha
  
#CadastroCliente
#idCliente:1 
#ClienteNome:PEDRO
#ClienteSobrenome:MARQUES
#ClienteCpf:06493600600 

  
  
   
  
 Cliente_Endereco
    idCliente_Endereco
    idCliente
    Cliente_EnderecoCep
    Cliente_EnderecoRua
    Cliente_EnderecoNumero
    Cliente_EnderecoComplemento
    Cliente_EnderecoBairro
    Cliente_EnderecoCidade
    Cliente_EnderecoEstado

#CADASTRO ENDEREÇO

#idCliente_Endereco: 1
#idCliente: 1
#Cliente_EnderecoCep:31910110    
#Cliente_EnderecoRua: RUA ARAUA
#Cliente_EnderecoNumero: 145
#Cliente_EnderecoComplemento : CASA/FUNDOS
#Cliente_EnderecoBairro: SAO PAULO
#Cliente_EnderecoCidade: BELO HORIZONTE
#Cliente_EnderecoEstado: MG    
 
    
Cliente_Contato
  idCliente_Contato
  idCliente
  Cliente_ContatoTelefone
  Cliente_ContatoWhatsapp
  Cliente_ContatoEmail
  
#idCliente_Contato: 1
#idCliente: 1
#Cliente_ContatoTelefone : 34325941
#Cliente_ContatoWhatsapp: 31984404639
#Cliente_ContatoEmail: pedro.hmo91@gmail.com

  
  
Carro
  idCarro
  CarroModelo = varchar
  CarroMotor = varchar
  CarroAno = int
  CarroVersao = varchar
  CarroKm = int
  CarroCombustivel =  ['Alcool','Gasolina','Flex']
  CarroCor = varchar
  CarroPortas =  ['2 portas','4 portas']

#idCarro: 1
#CarroModelo: Celta
#CarroMotor: 1.0 8v VHC
#CarroAno: 2004
#CarroVersao: SUPER
#CarroKm: 138.000
#CarroCombustivel: ['Gasolina']
#CarroCor: ['PRATA']
#CarroPortas:  ['2 portas']

  
Cliente_Carro1:
  idCliente_Carro1
  idCarro
  idCliente

#idCliente_Carro1: 1
#idCarro: 1
#idCliente: 1

  
  
#</Login>  





OleoMotor
  idOleoMotor
  idCarro
  OleoMotorProduto = FKidProduto ['oleo']
  OleoMotorCapacidade = varchar
  OleoMotorBujao = FKidProduto ['Bujao']
  OleoMotorFiltroOleo = FKidProduto ['Filtro de Oleo']
 

CarroArrefecimento
  idArrefecimento
  idCarro
  capacidadeSistema = varchar
  
  

CarroTabelaFipe
  idCarro
  CarroTabelaFipePreco
    
  
CarroDefeito
  idCarroDefeito
  idCarro
  idServico
  idProduto
  CarroDefeitoTitulo
  
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
  
  
