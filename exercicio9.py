for num in range(1, 10001):
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i

    if soma_divisores == num:
        print(f"{num} é um número perfeito!")
