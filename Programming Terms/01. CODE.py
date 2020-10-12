import logging

def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func
    

F_func = outer_func('Joseph')
L_func = outer_func('Yu')

F_func()
L_func()


def html_tag(msg_1):
    def wrap_txt(msg_2):
        print(f"<tag>msg</tag>")
    return wrap_txt
    
    
html_tag('Hello')('Emma')
html_tag('Hello')('Joseph')

html_tag('h1')('Header1')
html_tag('h2')('Header2')

html_tag('p1')('Paragraph1')
html_tag('P2')('Paragraph2')


logging.basicConfig(filename='01. Example.py', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(
        f"Running {func.__name__} with arguments {args}")
        print(func(*args))
    return log_func
    
    
def add(x, y):
    return x + y
    
    
def sub(x, y):
    return x - y
    
    
add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 5)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)
