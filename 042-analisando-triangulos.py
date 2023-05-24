lado1 = float(input("Primeiro segmento: "))
lado2 = float(input("Segundo segmento: "))
lado3 = float(input("Terceiro segmento: "))
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    if lado1 == lado2 == lado3:
        print(f"Os segmentos acima formam um triângulo EQUILÁTERO.")
    elif lado1 != lado2 and lado1 == lado3 or lado1 != lado3 and lado1 == lado2:
        print("Os segmentos acima formam um triângulo ISÓSCELES.")
    elif lado1 > lado2 > lado3 or lado2 > lado3 > lado1:
        print("Os segmentos acima formam um triângulo ESCALENO.")
else:
    print("Os segmentos acima NÃO FORMAM um triângulo.")
