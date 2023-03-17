# 2 -
def ack(m, n):
    if m < 0 or n < 0:
        print('Ackermann function is not defined for negative integers.')
        return None
    elif m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))


print(ack(-1, -2))


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('osso'))
print(is_palindrome('reviver'))