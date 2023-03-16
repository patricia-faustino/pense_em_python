# a recursão deve ter uma parada, caso contrário vira uma recursão infinita
# sempre é necessário validar se de fato a parada será atingida
def coutdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        coutdown(n - 1)


# coutdown(5)


def do_n(s, n):
    if n > 0:
        print(s)
        do_n(s, n - 1)


do_n('Hello', 2)
