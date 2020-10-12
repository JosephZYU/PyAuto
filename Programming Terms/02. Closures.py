"""
Recall from 02. First Class functions:

allow us to treat functions like any other objects

we can return functions and assign functions into variables


⚡🧠Closure: 

it is an inner function that remembers and has access to variables in the local scope which it was created 
even after the outer function has finished executing



A Closure closes over the FREE variables from their environment

In this case, message would be that free variable

"""


import logging


def outer_func(msg):
    message = msg

    # Define inner function - in this particular case there is no input variable
    # A Free Variable == NOT defined in the function but still have access to it
    def inner_func():
        print(message)

    # 1 of 2: return the function  w/ execution
    # return inner_func()

    # 2 of 2: return the function  w/out execution
    # NO execution, simply return the inner function
    return inner_func


# In 2 of 2: this my_func is a new function == outer_func() == inter_func

fn_func = outer_func('Joseph')
ln_func = outer_func('Yu')

fn_func()
ln_func()


# Translated from JavaScript Example

def html_tag(tag):
    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")
        # print("<{0}>{1}</{0}>".format(tag, msg))
    return wrap_text


html_tag('Hello!')('Emma')
html_tag('Hello!')('Joseph')

html_tag('h1')('Emma')
html_tag('h2')('Joseph')

html_tag('p1')('Test Paragraph')
html_tag('p2')('Test Paragraph')


# Closure - Snippet Example

logging.basicConfig(filename='01. Example.log', level=logging.INFO)


def logger(func):
    # 👀 Inner functions can take in any number of arguments: *args 🧠
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)
