
def calculadora(tipo):
    if tipo == 'soma':                   # Condição IF para verificar qual tipo de operação o usuário deseja
        def soma(*args):
            return sum(args)             # Somar e retornar os valores recebidos pelo *args
        return soma                      # Retornar o valor da soma

    elif tipo == 'subtrair':
        def subtrair(*args):
            valor = 0
            for item in args:                    # Looping para pegar todos os valores do *args individualmente
              if valor == 0 and item >= 1:       # Condição de iniciar
                  valor = item - valor           # Valor recebe item(valor que o usuário digitou) - valor
              else:
                  valor = valor - item           # Valor - item(segundo valor que o usuário digitou)
            return valor                         # Retorna o valor
        return subtrair                          # Retorna a função

    elif tipo == 'multiplicar':
        def multiplicar(*args):
            valor = 1
            for valores in args:                 # Looping para pegar todos os valores em args
                valor = valores * valor          # Variável valor vai receber cada valor de args * ela mesma.
            return valor                         # Retorna o valor
        return multiplicar                       # Retorna a função multiplicar

    elif tipo == 'dividir':
        def dividir(*args):
            valor = 0
            for item in args:                    # Looping para pegar todos os valores em args
                if valor == 0 and item > valor:  # Condição para iniciar o programa, irá passar aqui somente uma vez
                    valor = 1                    # Valor receberá o valor 1 para não apresentar erro de divisão por zero
                    valor = item / valor         # Valor vai receber o item / valor, no caso. item / 1
                else:                            # Valor será o número que o usuário digitar por primeiro.
                    valor = valor / item         # Se não, valor vai receber ele mesmo dividido por item
            return valor                         # Retorna o valor
        return dividir                           # Retorna a função dividir



tipo_operacao = input('Informe o tipo de operação: [adicionar/subtrair/multiplicar/dividir]: ')
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))


if tipo_operacao == 'adicionar':
    adicionar = calculadora('soma')   # Variável adicionar vai receber a função calculadora atribuida com tipo 'soma'
    print('\nVocê escolheu adição')
    print(f'O resultado da adição de {valor1} + {valor2} = ', adicionar(valor1, valor2))
    # Esse print acima vai imprimir os valores digitados pelo usuário em {valor1} + {valor2}
    # e vai atribuir a função adicionar os argumentos valor1, valor2 (No caso, os valores digitados lá em cima)

elif tipo_operacao == 'subtrair':
    subtrair = calculadora('subtrair')  # Variável subtrair vai receber a função calculadora atribuida com tipo 'subtrair'
    print('\nVocê escolheu subtração')
    print(f'O resultado da subtração de {valor1} - {valor2} =  ', subtrair(valor1, valor2))
    # Esse print acima vai imprimir os valores digitados pelo usuário em {valor1} + {valor2}
    # e vai atribuir a função subtrair os argumentos valor1, valor2.


elif tipo_operacao == 'multiplicar':
    multiplicar = calculadora('multiplicar') # Variável multiplicar vai receber a função calculadora atribuida com tipo 'multiplicar'
    print('\nVocê escolheu multiplicar')
    print(f'O resultado da multiplicação de {valor1} * {valor2} = ', multiplicar(valor1, valor2))
    # Esse print acima vai imprimir os valores digitados pelo usuário em {valor1} + {valor2}
    # e vai atribuir a função multiplicar os argumentos valor1, valor2.


elif tipo_operacao == 'dividir':
    try:                                   # Try irá tentar executar esse bloco de comando abaixo
        dividir = calculadora('dividir')   # Variável dividir vai receber a função calculadora atribuida com tipo 'dividir'
        dividir(valor1, valor2)      # Atribuindo os valores valor1, valor2 a função dividir
        print('\nVocê escolheu dividir')
        print(f'O resultado da divisão de {valor1} / {valor2} =', dividir(valor1, valor2))
        # O print acima se tudo funcionar corretamente irá imprimir os valores digitados pelo usuário em {valor1} + {valor2}
        # e vai atribuir a função dividir os argumentos valor1, valor2.
    except ZeroDivisionError:
        print('\nErro Divisão por zero')  # Se o Try não for executado por conta de divisão de zero
                                          # irá imprimir uma mensagem ao usuário informando sobre.