# Module à tester

def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b
