import math


def area(radius):
    return math.pi * radius**2


a = area(4)
print(a)


# toda zona que fica após o retorno, dependendo de qual condição x obedeça
# é chamada de zona morta
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


print(absolute_value(-5))

