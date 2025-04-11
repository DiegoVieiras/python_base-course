nome = "Diego"
sobrenome = "Santos"
ano_nascimento = int(input("Qual seu ano de nascimento? "))
idade = 2025 - ano_nascimento
maior_de_idade = idade >= 18
altura_metros = float(input("Qual sua altura em metros? "))

print('\n\nNome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)

if maior_de_idade == True:
    print('É maior de idade? Sim, é maior de idade')
else:
    print('É maior de idade? Não, é menor de idade')

print('Ano de nascimento: ', ano_nascimento)
print('Altura em metros: ', altura_metros,"\n\n")
