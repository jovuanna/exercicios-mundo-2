'''for a in range(1, 51):
        if a % 2 == 0:              #a cada laço de repetição ele verifica se a condição é verdadeira,
        print(a, end=' ')            e quando não é gasta mais processamento sem necessidade.
        print("Fim")
'''
#menos processamento
for a in range(2, 51, 2):
    print(a, end=' ')
print("Fim!")
