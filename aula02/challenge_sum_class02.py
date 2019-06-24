"""
# Dado uma matriz, calcular a soma das diagonais:

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Exemplo: 1+5+9+3+5+7
"""

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

a, b = 0, 0

for x,y in enumerate(matriz):

    a += y[x]
    b += y[-(x+1)]
    total = a+b

print(total)