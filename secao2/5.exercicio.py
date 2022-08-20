#5. Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa).

nome = (input("Digite o seu nome: "))
peso = (float(input("Qual é o seu peso?: ")))
altura = (float(input("Qual é a sua altura?: ")))

imc = peso / (altura ** 2)

print(f'O seu nome é {nome} e o seu IMC é {imc:.2f}.')