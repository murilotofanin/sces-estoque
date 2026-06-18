
##Tive ajuda do Miguel para fazer esse codigo e tambem do Kauan

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


def listarprodutos():
      print("Mostrando os produtos da lista!!")
      for i in estoque:
            print(i)

        
        
        
