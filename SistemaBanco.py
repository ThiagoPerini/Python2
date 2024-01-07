import time                                        # Importar módulo time para aguardar entre uma função e outra
print('|-----------------------|')
print('|                       |')
print('|Bem vindo ao Banco Ouro|')
print('|                       |')
print('|-----------------------|')
print('\n')
saldo = 0                                          # Variável que receberá todos os valores e alterações
while True:                                        # Looping infinito
    time.sleep(2)                                  # Tempo para imprimir as opções
    print('Qual opção deseja utilizar: \n'         
          '(1) Depositar\n'
          '(2) Sacar\n'
          '(3) Verificar saldo\n'
          '(4) Transferir\n'
          '(5) Sair')
    resposta = int(input('Opção: '))               # Variável que recebe um número inteiro de resposta
    if resposta == 1:                              # Primeira condição da variável
        valor_deposito = float(input('Digite o valor de deposito: '))
        if valor_deposito <= 0:                    # Tratamento de possíveis erros(Se valor de depósito for menor ou igual a zero
            time.sleep(1)                          # Tempo para imprimir a resposta
            print('Valor de depósito inválido!\n')
        else:
            saldo += valor_deposito                # Saldo que recebe ele mesmo + valor_deposito
            time.sleep(1)                          # Tempo para imprimir a resposta
            print(f'Valor R${valor_deposito:.2f} foi depositado!\n')

    elif resposta == 2:                            # Segunda condição da variável
        valor_saque = float(input('Informe o valor que deseja sacar: '))
        if valor_saque > saldo or valor_saque <= 0:  # Tratamento de erros
            time.sleep(1)                            # Tempo para imprimir a resposta
            print('Valor de saque inválido/saldo insuficiente!\n')
        else:
            saldo -= valor_saque                     # Saldo recebe saldo - valor_saque
            time.sleep(1)                            # Tempo para imprimir a resposta
            print(f'Saque de R${valor_saque:.2f} realizado!\n')

    elif resposta == 3:                             # Terceira condição da variável
        time.sleep(1)                               # Tempo para imprimir a resposta
        print(f'Seu saldo atual é de R${saldo:.2f} reais\n')

    elif resposta == 4:                             # Quarta condição da variável
        valor_transferir = float(input('Informe o valor da transferência: '))
        conta_transferir = input('Informe o número da conta que será feita a transferência: ')
        if valor_transferir > saldo:                # Condição se valor da transferência for maior que o saldo
            time.sleep(1)                           # Tempo para imprimir a resposta
            print('Erro na transferência, saldo insuficiente!\n')
        elif valor_transferir <= 0:                 # Condição se o valor da transferência for menor ou igual a zero
            time.sleep(1)                           # Tempo para imprimir a resposta
            print('Valor de transferência inválido!\n')
        else:
            saldo -= valor_transferir               # Saldo recebe saldo - valor_transferir
            time.sleep(1)                           # Tempo para imprimir a resposta
            print(f'O valor de R${valor_transferir:.2f} foi transferido para a conta {conta_transferir}\n')

    elif resposta == 5:                             # Quinta condição da variável
        time.sleep(1)                               # Tempo para imprimir a resposta
        print('Programa encerrado, até a próxima!')
        break                                       # Encerrar o looping
