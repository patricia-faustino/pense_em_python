def factorial(x):
    if x == 0:
        return 1
    else:
        recursive = factorial(x - 1)
        return recursive * x
    return x


print(factorial(4))
