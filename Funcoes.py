
def fabrica_de_operacoes(tipo):
    if tipo == 'soma':
        def soma(*args):
            return sum(args)
        return soma

    elif tipo == 'subtrair':
        def subtrair(*args):
            valor = 0
            valor2 = 0
            for item in args:
               if item > valor:
                   valor = item
               else:
                   valor2 = item
            return valor - valor2
        return subtrair

    elif tipo == 'multiplicar':
        def multiplicar(*args):
            valor = 1
            for valores in args:
                valor = valores * valor
            return valor
        return multiplicar

    elif tipo == 'dividir':
        def dividir(*args):
            valor = 1
            for item in args:
                if valor == 1 and item > valor:
                    valor = item / valor
                else:
                    valor = valor / item
            return valor
        return dividir



tipo_operacao = input('Informe o tipo de operação: [adicionar/subtrair/multiplicar/dividir]: ')
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))


if tipo_operacao == 'adicionar':
    operacao = fabrica_de_operacoes('soma')
    print(operacao(valor1, valor2))

elif tipo_operacao == 'subtrair':
    subtrair = fabrica_de_operacoes('subtrair')
    print('\nVocê escolheu subtração')
    print(f'O resultado da subtração de {valor1} - {valor2} =  ', subtrair(valor1, valor2))

elif tipo_operacao == 'multiplicar':
    multiplicar = fabrica_de_operacoes('multiplicar')
    print('\nVocê escolheu multiplicar')
    print(f'O resultado da multiplicação de {valor1} * {valor2} = ', multiplicar(valor1, valor2))

elif tipo_operacao == 'dividir':
    dividir = fabrica_de_operacoes('dividir')
    print('\nVocê escolheu dividir')
    print(f'O resultado da divisão de {valor1} / {valor2} = ', dividir(valor1, valor2))