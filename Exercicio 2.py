print("Peça ao usuário um número inteiro positivo, e calcule a soma de todos os números de 1 até N, usando while\n")

N = int(input("Digite um número inteiro e positivo: \n"))
soma = 0
contador = 1

if N > 0:
    while contador <= N:
        soma = soma + contador
        contador += 1
    print(f"A soma de todos os números de 1 até {N} é {soma}")

else:
    print("Inválido")
