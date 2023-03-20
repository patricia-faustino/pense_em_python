def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Acabou')


# countdown(100)

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1


# sequence(143)

# na recursividade deve haver um caso base(condição de parada) e ela deve realmente antigir o objetivo
# de para a execução de recursividade
def print_n(s, n):
    while n > 0:
        n -= 1
    print(s)


# print_n(2, 8)
print_n('Hello', 2)
