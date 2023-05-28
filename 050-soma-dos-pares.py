soma = 0
for a in range(0, 6):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
print(f"A soma dos números pares digitados é igual a {soma}.")
