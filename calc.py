print('---------------------- test project -------------------------------')
def add(a, b):
    if a > 0 and b > 0:
        return a + b
    else:
        return 'enter non zero values'

def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print(add(10, 10))
print(sub(50, 10))
print(multiply(10, 10))
print(divide(10, 2))
