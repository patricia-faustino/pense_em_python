import turtle

bob = turtle.Turtle()


def create_square(bob):
    sides = 4
    i = 1
    print(bob)

    while i <= sides:
        bob.fd(100)
        bob.lt(90)
        i += 1


create_square(bob)
turtle.mainloop()
