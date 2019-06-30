'''
O “finally” será executado independente da ocorrência ou não de exceção no seu código.
Significa, seja qual for o resultado do código, o que está abaixo dele será executado.
Podemos implementar o finally no exemplo anterior da seguinte forma:
'''

try:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print (x+y)
except Exception as e:
    print("Digite apenas números")
finally:
    print("Saindo do script")
