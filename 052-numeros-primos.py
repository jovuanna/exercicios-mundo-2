num = int(input("Digite um número: "))
cont = 0
for a in range(1, num + 1):
    if num % a == 0:
         print('\033[31m', end='')
         cont += 1
    else:
        print('\033[m', end='')
    print(a, end=' ')
print(f"\033[mO número foi divisível {cont} vezes.")
if cont == 2:
    print("O número é primo.")
else:
    print("O número não é primo.")
