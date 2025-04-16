n = int(input("Digite um valor: \n"))

a, b = 0, 1
i = 0

if n < 1:
    print("Inválido")
else:
    while i < n:
        print(a, end=' ')
        a, b = b, a + b
        i += 1
