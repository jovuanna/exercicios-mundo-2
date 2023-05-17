ValorCasa = float(input("Qual o valor da casa? "))
Salario = float(input("Quanto você ganha de salário? "))
Anos = int(input("Em quantos anos você deseja pagar? "))
Total = ValorCasa / (Anos * 12)
SalarioPorc = (Salario * 30) / 100
if Total >= SalarioPorc:
    print("Empréstimo negado!")
else:
    print("Empréstimo aprovaodo!")
