"""
Immutable 🆚 Mutable

⚡

To change a value in-place == Mutable

Specially, they needs to have the SAME Memory ID Address

"""

a = 'Corey'

# Print the Memory Address of variable
print(f"Memory Address of {a} is: {id(a)}")

"""
String is Immutable

a[0] = 'c'

👀 We can NOT force assign value "within" a string

print(f"Memory Address of {a} is: {id(a)}")


'str' object does not support item assignment

"""

a = [1, 2, 3, 4, 5]

print(f"Memory Address of {a} is: {id(a)}")

# Assign 1st item to a different value

a[0] = 6

print(f"Memory Address of {a} is: {id(a)}")
