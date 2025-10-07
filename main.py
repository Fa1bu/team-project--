def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b

if __name__ == "__main__":
    print("Hello, Team!")
    print("3 * 4 =", multiply(3, 4))
    print("8 / 2 =", divide(8, 2))
