#Exemplo de como escrever em um arquivo com python
#!/usr/bin/python3

with open ('frutas.txt','w') as arq:
    arq.write('limao\n')
    arq.write('melancia')

