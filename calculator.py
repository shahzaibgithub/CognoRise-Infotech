#calcaulator
print(
    '''
    Welcome to Calculator Application
    
    '''
)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator():
    operations = [add, subtract, multiply, divide]

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter choice (1/2/3/4): ")) - 1
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Call the function by indexing into the list
    result = operations[choice](num1, num2)
    return result

# Call the calculator function to run the calculator
print("Result:", calculator())


