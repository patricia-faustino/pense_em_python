x = 7
y = 8

print(x > 0 and y < 2)
print(x > 0 or y < 2)
print(not(x > 0))

# deve-se ter cuidado porque em python, na maioria dos casos, ao comparar preposições que não são
# do tipo booleano, o resultado será true
# o único resultado que é considerado como false é o número zero
print(42 and True)
print(0 and True)