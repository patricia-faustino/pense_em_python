x = 8
y = 8

# cada condição é chamada de ramo, no caso abaixo temos dois ramos, sendo que o último possui mais dois ramos
# mesmo sendo uma possibilidade, é indicado evitar as condições aninhadas por dificultar a legibilidade do código
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

z = 4
k = 8

# essas primeiras condições podem ser substituídas pela segunda
if 0 < z:
    if z < 10:
        print('x is a positive single-digit number.')

if 0 < z and z < 10:
    print('x is a positive single-digit number.')
    
# pode ser substituída também, por:
if 0 < z < 10:
    print('x is a positive single-digit number.')