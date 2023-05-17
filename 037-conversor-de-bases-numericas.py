num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para comversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opcao = int(input("Digite a sua opção: "))
if opcao == 1:
    b = bin(num).replace('0b', '') # a função 'bin' transforma o número em binário, mas aparece o '0b' na frente entaão replace serve pra retirar.
    print(f"{num} convertido para BINÁRIO é igual a: {b}")
elif opcao == 2:
    o = oct(num).replace('0o', '')
    print(f"{num} convertido para OCTAL é igual a: {o}")
elif opcao == 3:
    h = hex(num).replace('0x', '')
    print(f"{num} convertido para  HEXADECIMAL é igual a: {h}")
else:
    print("Erro! Digite uma opção válida.")