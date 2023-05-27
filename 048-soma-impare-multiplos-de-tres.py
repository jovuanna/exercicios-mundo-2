soma = 0
cont = 0
for a in range(1, 501, 2):
    if a % 3 == 0:
        cont += 1 #conta quantos números múltiplos de 3 e ímpares existem entre 1 e 500.
        soma += a #soma esses valores
print(f"A soma de todos os {cont} valores múltiplos de 3 entre 1 e 500 é igual a {soma}.")

