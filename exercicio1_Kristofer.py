# Exercicio 1 Algoritimos 2:
# Aluno Kristofer R.K
"""
Construir um algoritmo que contenha 3 listas:
•  Nomes de produtos
•  Preços de cada produto
•  Quantidades de cada produto
Construir uma função para imprimir um dos produtos da lista e uma
função para retirar um dos produtos das listas
"""
#Listas
lstNome = ['SABÃO', 'PAPEL', 'CADERNO']
lstValorUnit = [4.0, 3.0, 8.0]
lstQtd = [6, 8, 3]

#Variáveis:
y = 0
resultquantidade = 0

#Funções:

#Def imprimir um produto:
def imprimir_produto():
    nome = str(input('Digite o nome do produto a ser listado: '))
    nome = nome.upper()
    print("Modelo","Valor","Quantidade")
    for x in range(len(lstNome)):
        if nome in lstNome:
            localizar = lstNome.index(nome)
            print(lstNome[localizar], '  ', lstValorUnit[localizar],'     ', lstQtd[localizar])
            break
        else:
            print('Produto não encontrado!')
            break

#Def removerProduto:
def removeerProduto():
    nome = str(input('Digite o produto a ser retirado: '))
    nome = nome.upper()
    escolha = int(input('Você deseja retirar uma unidade (Digite 1), ou retirar todo o produto (Digite 2) ? '))
    if escolha == 1:
        for x in range(len(lstNome)):
            if nome in lstNome:
                localizar = lstNome.index(nome)
                lstQtd[localizar] = lstQtd[localizar] - 1
                print('Novo')
                print("Modelo","Valor","Quantidade")
                print(lstNome[localizar], '  ', lstValorUnit[localizar],'     ', lstQtd[localizar])
                break
            else:
                print('Erro')
    elif escolha == 2:
        for x in range(len(lstNome)):
            if nome in lstNome:
                localizar = lstNome.index(nome)
                lstNome.remove(nome)
                del lstValorUnit[localizar]
                del lstQtd[localizar]
                print('Produto removido com sucesso!')
                break
            else:
                print('Erro')
                
                
#Def Menu:
def escolherMenu():
    print("\n")
    menu = 8
    while menu != 0:
        print("===================================================================")
        print("                   Bem vindo a loja do Tio Kris                     ")
        print("===================================================================")
        print("Menu")
        print("0- Sair")
        print("1- Imprimir Produto")
        print("2- Remover produto")
        menu = int(input("Escolha: "))

        if menu == 0:
            print("Você fechou o programa!")
            break

        elif menu == 1:
            imprimir_produto()

        elif menu == 2:
            removeerProduto()

        else:
            print("Opção inexistente, voltando ao menu")
            print("\n")


escolherMenu()
