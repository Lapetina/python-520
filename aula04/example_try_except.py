'''
Exemplo - Tratamento de exceções

Existem diversos tipos de exceções que conseguimos manipular, evitando,
caso ocorram em um trecho de código, que o nosso script seja finalizado.

Para isto, usaremos o try / except

'''
#!/usr/bin/python3

while True:
    try:
        x = int(input("digite o primeiro número: "))
        y = int(input("digite o segundo número: "))
        print(x+y)
    except Exception as e:
        print("digite apenas números")
