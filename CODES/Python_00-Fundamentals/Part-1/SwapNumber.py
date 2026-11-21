# Swap values of Two numbers

#Method 1: Using a temporary variable
a = 5
b = 10
c = a

a = b
b = c
print("After swapping:")
print("a =", a)
print("b =", b)

#Method 2: Without using a temporary variable (using arithmetic operations)
x = 15
y = 25
x = x + y
y = x - y
x = x - y

# or in single line: x, y = y, x
# i.e. here we are using tuple unpacking to swap the values of x and y without using a temporary variable.
# i.e. we are creating a tuple (y, x) and then unpacking it into the variables x and y.

print("After swapping:")
print("x =", x)
print("y =", y)