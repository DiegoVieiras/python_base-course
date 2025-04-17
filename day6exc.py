nome = input('Digite seu nome: ')

if nome:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]} ")
    print(f"Seu nome tem {len(nome)} letras")
    if " " in nome:
        print("Seu nome tem espaço!")
    else:
        print("Seu nome não tem espaço!")

    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A última letra do seu nome é: {nome[-1]}")
else:
    print("\n##Desculpe, você deixou campos vazios.##\n")










