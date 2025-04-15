altura = 1.80
peso = 101
imc = peso // (altura**2)

print(f'\nMeu IMC é:  {imc:.0f}\n')

# Usando metodo .format()
meu_imc = '\nMeu IMC é: {:.0f}\n'.format(imc)

print("Usando o método ----->",meu_imc)
