while True:
    num1 = float(input("Enter first number: "))
    op = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    def add(a, b): return a + b
    def sub(a, b): return a - b
    def mul(a, b): return a * b
    def div(a, b): return a / b if b != 0 else "Error: Division by zero is not allowed."

    switch = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    if op in switch:
        result = switch[op](num1, num2)
        print("Result:", result)
    else:
        print("Invalid operator.")

    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        print("Calculator stopped.")
        break