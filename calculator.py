def add(x, y):
    """Returns the sum of x and y."""
    return x + y

def subtract(x, y):
    """Returns the difference of x and y."""
    return x - y

def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

def divide(x, y):
    """Returns the quotient of x and y."""
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def get_number(prompt):
    """Validates numeric input."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\n===== Calc Master (Calc is short for Calculator) =====")
        print("+  Addition")
        print("-  Subtraction")
        print("*  Multiplication")
        print("/  Division")
        print("x  Exit")
        choice = input("Choose an operation (+, -, *, /, x): ")

        if choice == "+":
            x, y = get_number("1st Number to add: "), get_number("2nd Number to add: ")
            print(f"Result: {add(x, y)}")
        elif choice == "-":
            x, y = get_number("1st Number to subtract: "), get_number("2nd Number to subtract: ")
            print(f"Result: {subtract(x, y)}")
        elif choice == "*":
            x, y = get_number("1st Number to multiply: "), get_number("2nd Number to multiply: ")
            print(f"Result: {multiply(x, y)}")
        elif choice == "/":
            x, y = get_number("1st Number to divide: "), get_number("2nd Number to divide: ")
            print(f"Result: {divide(x, y)}")
        elif choice == "x":
            print("See Ya Later!")
            break
        else:
            print("Inconceivable option. Please choose +, -, *, /, or x.")

if __name__ == "__main__":
    main()