def square(x):
    return x * x
    
    
def cube(x):
    return x * x * x


def remainder(x):
    return x % 2


def floored_division(x):
    return x // 2


# 1 of 2: passing a function as an argument to another function


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4, 5])

print(squares)

cubes = my_map(cube, [1, 2, 3, 4, 5])

print(cubes)

remainders = my_map(remainder, [1, 2, 3, 4, 5])

print(remainders)

floored_divisions = my_map(floored_division, [1, 2, 3, 4, 5])

print(floored_divisions)


# 2 of 2: to return a function from another function


def logger(msg):
    def log_message():
        print(f"Log: {msg}")
    return log_message

log_hi = logger('Hi!')

print(log_hi)

log_hi()

print(logger('Joseph'))

logger('Joseph')()


logger("Without function save into function!")()


# NEW example


def html_tag(tag):

    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")
    return wrap_text


html_tag('Morning')('Joseph')

html_tag('h1')('Test Headline!')

html_tag('h2')('Another Headline!')
