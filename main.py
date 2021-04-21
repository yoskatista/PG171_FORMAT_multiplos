pessoas_restaurante = int(input("Olá, bem vindo ao nosso restaurante\n Vocês estão em Quantas pessoas? "))

if pessoas_restaurante >= 8:
    print("Espere um momento que disponibilizaremos uma mesa já!!!")
else:
    print('Opa temos mesa por aqui')

numeros_multiplos = int(input("fale um numero agora e vamos ver se é multiplo de dez"))

calculo = numeros_multiplos % 10

if calculo == 0:
    print('Seu numero é multiplo de dez')
else:
    print('Não é um numero multiplo de dez')