#travei nesse por causa da matemática
print('='*20)
print("10 TERMOS DE UMA P.A")
print('='*20)
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (10 - 1) * razao
for a in range(termo, decimo + razao, razao):
    print(a, end=' ')
