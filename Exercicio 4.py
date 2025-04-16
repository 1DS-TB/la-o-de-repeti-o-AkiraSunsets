print("fatorial usando while ou for")

num = int(input("Digite um número: \n"))
resultado = 1
contador = 1
if num < 0:
    print("INVÁLIDO")
else:
    while contador <= num:
        resultado *= contador
        contador += 1
    print(f"O fatorial de {num} é {resultado}")
