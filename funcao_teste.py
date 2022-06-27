def math():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    operacao = str(input("Digite a operação: "))

    if operacao == 'soma':
        print (num1 + num2)

    elif operacao == 'menos':
        print (num1 - num2)

math()