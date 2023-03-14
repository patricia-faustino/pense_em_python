import math


def print_twice(bruce):  # argumento pode ser de qualquer tipo
    print(bruce)
    print(bruce)


# o argumento é avaliado somente uma vez antes da função ser chamada
print_twice(54)
print_twice(3.2)
print_twice('Olá')
print_twice('Olá ' * 4)

aleatorio = 'aleatorio '
print_twice(aleatorio)
print_twice(aleatorio * 4)
print(math.cos(math.pi))
