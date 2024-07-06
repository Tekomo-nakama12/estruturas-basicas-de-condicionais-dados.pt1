nome_pessoa = input("Digite o nome da pessoa: ")
peso = float(input("Digite o peso da pessoa: "))
altura = float(input("Digite a altura da pessoa: "))
imc = peso/altura**2
print (f"{imc}")

if imc < 18.5:
    print(f"O usuario  {nome_pessoa} com o IMC de {imc} está com a condição de  magreza")

elif imc >= 18.5 and imc <= 24.9:
    print(f"O usuario  {nome_pessoa} com o IMC de {imc} está classificado com peso normal")

elif imc > 24.9 and imc < 29.9:
    print(f"O usuario  {nome_pessoa} com o IMC de {imc} está  com asobrepeso")

elif imc >= 29.9 and imc < 34.9:
    print(f"O usuario  {nome_pessoa} com o IMC de {imc} está classificado com obesidade  I")

elif imc > 34.9 and imc <= 40:
    print(f"O usuario  {nome_pessoa} com o IMC de {imc} está classificado com obesidade  II")

else:
    print(f"O usuario {nome_pessoa} com o IMC de {imc} está classificado com obesidade  III")