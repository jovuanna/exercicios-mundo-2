from time import sleep
num = int(input("Digite um número para verificar sua tabuada: "))
for a in range(1, 11):
    print(f"{num} X {a} = {num * a}")
    sleep(0.5)
