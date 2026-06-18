
##Tive ajuda do Miguel e do Gustavo Dias

estoque = [
     [1,"Volante", 2, "Prateleira01"],
     [2,"Sapato", 4, "Prateleira02"],
     [3,"Ecapamento", 5, "Prateleira03"],
     [4,"Capô", 8, "Prateleira04"],
     ]



proximoID = 5


def adicionarProdutos():
        global proximoID   
        id_item = int(input("Digite o ID: "))
        nome = input("Digite o nome: ")
        quantidade = int(input("Digite a quantidade: "))
        localizacao = input("Digite a localização: ")

        produto = [id_item, nome, quantidade, localizacao]

        estoque.append(produto)
        proximoID = proximoID + 1

        print("Produto adicionado!👍👍")
def travarmenu():
     input("\nPrecisione p botão enter para continuar!!")

def listarprodutos():
      print("Mostrando os produtos da lista!!")
      for i in estoque:
            print(i)

def BuscarID():
        buscaproduto = int(input("Digite o ID do produto: "))
        posicaoProcurado = -1

        for i in range(len(estoque)):
            if(estoque[i][0] == buscaproduto):
                posicaoProcurado = i
        if (posicaoProcurado == -1):
                print("Produto não encontrado!!☢️")
        else:
             print(f"O produto é {estoque[buscaproduto]}")

def atualizarEstoque():
    idProduto = int(input("Qual o novo ID do produto?:"))
    linhaProcurada = -1
    for i in range(len(estoque)):
        if(estoque[i][0] == idProduto):
            linhaProcurada = i
    print(f"O produto atualizado é {estoque[linhaProcurada]}")
    quantidade = int(input("QUAL A QUANTIDADE DO PRODUTO?: "))
    estoque[linhaProcurada][2] = quantidade

def excluirProdutos():
     idProduto = int(input("Qual é o ID do produto que você deseja Excluir?:"))
     linhaProcurada = -1
     for i in range(len(estoque)):
        if(estoque[i][0] == idProduto):
          linhaProcurada = i
          print(linhaProcurada)
          if(linhaProcurada == -1):
                print("Produto não encontrado!!☢️")
        else:
          Apagar=input("Você quer excluir esse produto? Sim/Não ").capitalize()
          if (Apagar=="Sim"):
                estoque.pop(linhaProcurada)
                print("Produto excluido com sucesso 🗑️")
          else:
                print("Cancelado !!")
                travarmenu()
          

     


while True:

    print("\n----------MENU DO ESTOQUE---------")
    print("1 - Adicionar Produto | 2-Lista de Produtos | 3-Buscar produtos por ID | 4- Atualizar estoque |5-Excluir Produtos | 6-Sair "  )
    opcao = input("Escolha uma opção abaixo: ")
    if(opcao == "1"):
        adicionarProdutos()

    elif(opcao == "2"):
        listarprodutos()


    elif(opcao == "3"):
        BuscarID()


    elif(opcao == "4"):
         atualizarEstoque()

    elif(opcao == "5"):
     excluirProdutos()
     
    elif(opcao == "6"):
        print("Finalizando o Sistema!!")
        break
        
        
