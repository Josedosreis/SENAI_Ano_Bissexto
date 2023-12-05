# Ano bissexto

# Apresentaçao

print('\n\t\t --- Ano bissexto --- \n')

# Entrada

print(f'>>>>> Qual ano você que saber se é Bissexto ou não?')

ano = int(input('Digite o ano: '))

# Processamento c/ # Saída

bissexto = ano % 4

if bissexto == ano % 4 == 0:
    print(' >>> O Ano é Bissexto ! <<< ')
else:
    print(' >>> O ano não é Bissexto ! <<< ')



