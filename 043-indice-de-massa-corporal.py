peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / altura ** 2
print(f"Olá! Seu imc é {imc:.1f}.")
if imc <= 18.5:
    print(f"Cuidado! Você está muito abaixo do peso, procure um médico.")
elif imc <= 25:
    print("Parabéns! Você está no peso ideal.")
elif imc <= 30:
    print("Cuidado! Você está em sobrepeso.")
elif imc <= 40:
    print("Cuidado! Você está obeso.")
else:
    print("Cuidado! Você está com obesidade móbida, procure um médico.")