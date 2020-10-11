"""
✅ Try to define more functions and pass into the my_map()
✅ Division 🆚 Floor Division (Integer Division) 🆚 Remainder 
✅ Review on the difference between result.append 🆚 result.extend
"""

"""
First-Class Functions will help you understand other terms such as:

higher water functions
currying
closures

"""


def square(x):
    return x * x


# 👀 with () parenthesis mean we will execute the function ✔
# 👀 Without () parenthesis mean we will store the function into another variable 🤏

# f = square(5)
# Now we can treat the variable f as a function

f = square

print(square)
print(f)
print(f(5))


def cube(x):
    return x * x * x


def remainder(x):
    return x % 2


def floored_division(x):
    return x // 2


"""
Higher-order function:
we can also pass functions as arguments and return functions as the result of other functions

😎 The great thing about Higher-order func is to dynamically place function into another func without renaming it everytime

We can now pass any function into our custom map function we created

👍 Great for Speed, Code Readability, and Efficiency ⚡
"""

# 1 of 2: passing a function as an argument to another function


def my_map(func, arg_list):
    # Create an empty result array
    result = []
    # Loop through all items in the passed in array
    # Run each of those items through the "func" that we passed in as an argument
    # Append that to the result
    for i in arg_list:
        result.append(func(i))
    return result


# 🧐 NOTE: we are NOT including () when passing the square function❗
# We are NOT executing the function itself, but to pass in the function as a pre-defined logic from above
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

    # ❗ Within this function, we have another function
    # 👀 This function does NOT take in any argument
    def log_message():
        print(f"Log: {msg}")

    # We're returning a function within a function
    # 👀 NO parenthesis ()
    return log_message


# Save log_hi variable == log_message()

log_hi = logger('Hi!')

# log_hi is the function NOT executed yet
print(log_hi)

log_hi()

# logger('Joseph) is another "function" to be executed
print(logger('Joseph'))

logger('Joseph')()


logger("Without function save into function!")()

# NEW example


def html_tag(tag):

    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")

        # Sometimes it's great to use format with Reg X
        # print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text


html_tag('Morning')('Joseph')

html_tag('h1')('Test Headline!')

html_tag('h2')('Another Headline!')
