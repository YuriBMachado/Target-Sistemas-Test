def fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num or num == 0:
        return f"O numero {num} pertence a fibonacci"
    else:
        return f"O numero {num} não pertence a fibonacci"


# Exemplo
numero = int(input("Informe um número: "))
print(fibonacci(numero)) 