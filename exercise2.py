def fibonacci_sequence(n):
    # Função para gerar a sequência de Fibonacci até o número n
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def is_fibonacci(n):
    fib_sequence = fibonacci_sequence(n)
    if n in fib_sequence:
        return True
    else:
        return False

# Solicitar o número ao usuário
n = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verificar se o número pertence à sequência
if is_fibonacci(n):
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} NÃO pertence à sequência de Fibonacci.")

