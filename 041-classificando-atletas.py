ano = int(input("Ano de nascimento: "))
idade = 2023 - ano
if idade <= 9:
    print(f"Atleta com {idade} anos. Categoria MIRIM.")
elif idade <= 14:
    print(f"Atleta com {idade} anos. Categoria INFANTIL.")
elif idade <= 19:
    print(f"Atleta com {idade} anos. Categoria JUNIOR.")
elif idade <= 25:
    print(f"Atleta com {idade} anos. Categoria SÊNIOR.")
else:
    print(f"Atleta com {idade} anos. Categoria MASTER.")
