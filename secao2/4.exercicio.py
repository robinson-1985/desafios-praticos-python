#3. Obter o ano de nascimento da pessoa(baseado na idade e no ano atual).

nome = (input("Digite o seu nome: "))
idade = (int(input('Qual é a sua idade? - ')))
ano_atual = (int(input('Qual é o ano atual? - ')))

nascimento = ano_atual - idade

print(f'{nome} nasceu em {nascimento}')