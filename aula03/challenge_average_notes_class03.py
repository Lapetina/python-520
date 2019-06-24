"""
Neste desafio iremos treinar o conhecimento que adquirimos na Aula de Manipulando arquivos.

Faça um programa que leia 4 notas de um aluno e calcule a média, e faça a seguinte validação:

Nota igual ou maior que 7 aprovado
Notas menor que 7
Maior que 3 recuperação
Notas menores ou igual a 3 reprovado.

Deve utilizar entrada de dados para obter as notas,
calcular a média e ter a saída utilizando bloco de condição para validar se o aluno foi aprovado ou não.
"""

def student_status(medium):
    if medium >= 7:
        print("Sua nota foi {:.2f}, você está aprovado!".format(medium))
    elif medium <7 and medium>3:
        print("Sua nota foi {:.2f}, você está de recuperação! ".format(medium))
    else:
        print("Sua nota foi {:.2f}, você está reprovado! ".format(medium))

name = input("Qual o nome do aluno? \n")
school_notes = []
x = 0
m = 0

while x < 4:
    n = input("Informe a nota do aluno: ")
    school_notes.append(n)
    x += 1

school_notes = map(int,school_notes)

for x in school_notes:
    m = m + x

medium = (m/4)

student_status(medium)