ano = int(input("Ano de nascimento: "))
idade = 2023 - ano
if idade < 18:
    print(f"Você se alistará em {18 - idade} anos.")
    print(f"Seu alistamento será em {(18 - idade) + 2023}")
elif idade == 18:
    print(f"Você já pode se alistar pois já tem 18 anos.")
else:
    print(f"Você tem {idade} e deveria ter se alistado a {idade - 18} anos.")

print(f"Quem nasceu em {ano} tem {idade} anos em 2023.")
