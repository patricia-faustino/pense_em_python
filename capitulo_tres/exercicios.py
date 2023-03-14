# 1
def right_justify(s):
    s_length = len(s)
    col_length = 70
    justify = col_length - s_length
    i = 1
    space = ''
    while i <= justify:
        space = space + ' '
        i += 1
    print(space + s)


print("1 - ")
right_justify('start')

# 2
print()
print("2 - ")


def print_spam(spam):
    print(spam)


def do_twice(function, spam):
    function(spam)
    function(spam)


def do_four(function, spam):
    do_twice(function, spam)
    do_twice(function, spam)


do_twice(print_spam, 'spam')
do_four(print_spam, 'spam')

print()
print('3 - ')


def build_grid():
    build_line_underscore_more()
    build_line_pipe_space(4, 10)
    build_line_underscore_more()
    build_line_pipe_space(4, 10)
    build_line_underscore_more()


def add_space(quantity_space):
    i = 1
    space = ''
    while i < quantity_space:
        space += ' '
        i += 1
    return space


def build_line_pipe_space(quantity_pipes, quantity_characters):
    i = 1
    pipe = '|'
    spaces = add_space(quantity_characters)
    pipe_space_line = (pipe + spaces) * 3

    while i <= quantity_pipes:
        print(pipe_space_line)
        i += 1


def build_line_underscore_more():
    more = '+ '
    underscore = '- '
    underscore_more_line = ((more + (underscore * 4)) * 2) + more
    print(underscore_more_line)


build_grid()
