itens = []
opcao = 0
while ( ( opcao >= 1 ) or ( opcao <= 5 ) ) :
    opcao = int(input('Selecione a opção desejada: \n' + 
                    '1- Listar   2- Cadastrar \n' + 
                    '3- Excluir  4- Alterar \n' +
                    '        5- Sair\n' + 
                    '-----------------------------\n' ))  
    if ( opcao == 1 ):
        print(listar())
    elif ( opcao == 2 ):
        item = input('Informe o nome do item para cadastrar: ')
        print(cadastrar(item))
    elif ( opcao == 3 ):
        item = input('Informe o nome do item para excluir: ')        
        print(excluir2(item))
    elif ( opcao == 4 ):
        if ( len(itens) == 0 ):
            print('A lista está vazia')
        else:
            item = input('Informe o nome do item que deseja alterar: ')
            print(alterar(item))
    elif ( opcao == 5 ):
        break
    else:
        print('Opção inválida')