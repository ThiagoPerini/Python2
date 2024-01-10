Agenda = {}

def mostrar_menu():
    print('\nMenu:\n'
          '1. Adicionar Contato\n'
          '2. Alterar Contato\n'
          '3. Remover Contato\n'
          '4. Listar Contatos\n'
          '5. Sair')
    

def opcoes(num):

    if num == 1:
        contato = input('Digite o nome do contato: ')
        numero = int(input('Digite o numero de telefone: '))
        print('\nContato adicionado com sucesso!')
        Agenda[contato] = numero

    elif num == 2:
        contato_existente = input('Digite o nome do contato que deseja alterar: ')
        if contato_existente in Agenda.keys():
            novo_contato = input('Digite o novo nome para o contato(Deixe em branco para não alterar): ')
            novo_numero = input('Digite o novo numero para o contato(Deixe em branco para não alterar): ')
            if novo_contato != '':
                Agenda[novo_contato] = Agenda[contato_existente]
                Agenda.pop(contato_existente)
            if novo_numero != '' and novo_contato != '':
                Agenda[novo_contato] = novo_numero
            elif novo_numero != '':
                Agenda[contato_existente] = novo_numero
        else:
            print('\nContato Inexistente!')
    elif num == 3:
        contato_remover = input('Digite o nome do contato que deseja remover: ')
        if contato_remover in Agenda.keys():
            Agenda.pop(contato_remover)
            print('\nContato removido com sucesso!')
        else:  
         print('\nContato não encontrado!')
    elif num == 4:
        if not Agenda.items():
            print('Nenhum contado encontrado!')
        for nome, numero in Agenda.items():
            print(f'\nNome: {nome} \nTelefone: {numero}')

    

while True:
    mostrar_menu()
    opcao = int(input('Escolha uma opção: '))           
    tipo = opcoes(opcao)
    if opcao == 5:
        break