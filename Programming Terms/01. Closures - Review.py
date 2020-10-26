

"""def outer_func():
    message = 'Joseph'
    print(message)


outer_func()"""


"""def outer_func():
    message = 'Morning Joseph!'

    def inner_func():
        print(message)

    return inner_func()


outer_func()"""

# Let's define the message we want to pass in
# This time they all take in a string argument

# 🧐 use simply short letters in the (msg)
# 👀 use longer version of message in the actual functions


"""def outer_func(msg):
    message = f"AWS {msg}"

    def inner_func(tag):
        print(f"{message} is the new {tag}")

    return inner_func


outer_func("Morning")("Joseph")"""


def outer_func(msg, tag):
    message = f"AWS {msg}"

    def inner_func():
        print(f"{message} is the new {tag}")

    return inner_func()


outer_func("Morning", "Joseph")

# outer_func('Hi!')
# outer_func('Hello!')
# outer_func('Morning!')

# 🧐 Why do we need outer and inner function in the first place?

# Separate outer and inner logic
# Great for re-use of partical code
# Break your code into manipulable chunks


"""def html_tag(tag):
    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")
    return wrap_text


h1 = html_tag('h1')
h2 = html_tag('h2')
h3 = html_tag('h3')

h1('Joseph')
h2('Joseph')
h3('Joseph')

h1('Corey')
h2('Corey')
h3('Corey')

h1('Shafer')
h2('Shafer')
h3('Shafer')

html_tag('p1')('Joseph')
html_tag('p2')('Corey')
html_tag('p3')('Shafer')"""


# ✅ Why do we NOT placing the () in the end this time
# Because this time it is NOT free "Empty" argument anymore, it does pass some new argument of its own
# If you pass your OWN argument, there should be NO () in the end


# 👀 Sample 1 of 2: with ()
# ⚡🧠 Empty == Empty; () == ()

def html_tag(msg, tag):
    def wrap_text():
        print(f"<{msg}>{tag}</{msg}>")
    return wrap_text()


html_tag('h1', 'p1')


# 👀 Sample 2 of 2: without ()
# ⚡🧠 something in the (msg) == return  function


def html_tag(msg):
    def wrap_text(tag):
        print(f"<{msg}>{tag}</{msg}>")
    return wrap_text


html_tag('h1')('p1')
