def introducao():
    print('-'*20)
    print(f"LOJA DA GIOVANNINHA")
    print('-'*20)


introducao()
preco = float(input("Preço das compras: R$"))
print('''
[ 1 ] À vista (dinheiro ou cheque)
[ 2 ] Débito
[ 3 ] Crédito (2x)
[ 4 ] Crédito (3x ou mais)
''')
opcao = input("Digite a opção desejada: ")
if opcao == "1":
    desconto = preco - ((preco * 10) / 100)
    print(f"Sua compra foi efetuada! Você recebeu um desconto de 10% e o total da compra foi R${desconto}. Volte sempre!")
elif opcao == "2":
    desconto = preco - ((preco * 5) / 100)
    print(f"Sua compra foi efetuada! Você recebeu um desconto de 5% e o total da compra foi R${desconto}. Volte sempre!")
elif opcao == "3":
    parcelas = int(input("Digite quantas parcelas deseja dividir a compra: "))
    if parcelas > 2:
        print("Erro! Digite uma opção válida.")
    else:
        preco_parcela = preco / parcelas
        print(f"Sua compra foi efeutada! Você escolheu {parcelas} parcelas. Cada uma ficou no preço de R${preco_parcela:.2f} e o valor total da compra foi de R${preco}. Volte sempre!")
elif opcao == "4":
    parcelas = int(input("Digite quantas parcelas deseja dividir a compra: "))
    if parcelas < 3:
        print("Erro! Você digitou a opção errada.")
    else:
        preco_total = (preco * 20) / 100 + preco
        preco_parcela = preco_total / parcelas
        print(f"Sua compra foi efetuada. Você escolheu {parcelas}. Cada uma ficou no preço de R${preco_parcela} você recebeu um juros de 20%, o preço total da sua compra foi de R${preco_total}. Volte sempre!")
else:
    print("Erro! Digite uma opção válida.")
