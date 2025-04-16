num = int(input("Digite o primeiro número: \n"))

print(f"Números primos entre {num}")

for numero in range(num + 1):
    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                break
        else:
            print(numero)
