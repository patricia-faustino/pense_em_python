# condições/partes do código que previnem erros é chamada de guardião
# pré-condição: erro ao chamar a função, erro nos argumentos
# pós-condição: erro na função
def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial('aa'))
print(factorial(5.0))
print(factorial(4))
print(factorial(-4))
print(factorial(0))