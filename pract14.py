def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate():
    a = int(input("Enter a number: "))
    b = input("Enter another number: ")
    total = add(a, b)
    product = multiply(a, b)
    print(f"The sum of {a} and {b} is {total} and the product is {product}")

calculate()
