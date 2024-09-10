# Sequência de Fibonacci

# Função que calcula o valor da sequência de Fibonacci, dado um índice n
def fibonacci(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

# Entrada
n = int(input("Entre com um numero: "))

# Variáveis auxiliares
sequencia = []
aux = 0
i = 0

# Calcula a sequência de Fibonacci até encontrar (ou não) o número de entrada
while aux <= n:
    aux = fibonacci(i)
    sequencia.append(fibonacci(i))
    i += 1
    if aux == n:
        break
    
# Saída
if n in sequencia:
    print("O numero faz parte da sequencia de Fibonacci!")
    
else:
    print("O numero nao faz parte da sequencia de Fibonacci!")