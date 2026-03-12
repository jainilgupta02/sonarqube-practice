RESULT = "Result:"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


if __name__ == "__main__":
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose operation (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(RESULT, add(num1, num2))
    elif choice == '2':
        print(RESULT, subtract(num1, num2))
    elif choice == '3':
        print(RESULT, multiply(num1, num2))
    elif choice == '4':
        print(RESULT, divide(num1, num2))
    else:
        print("Invalid choice")