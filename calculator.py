def add(x, y):
    """Returns the sum of x and y."""
    return x+y 

def subtract(x, y):
    """Returns the difference of x and y."""
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    pass  # implemented in division branch

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
        print("\n===== Calculator Master =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == "1":
            x, y = get_number("Enter first number: "), get_number("Enter second number: ")
            print(f"Result: {add(x, y)}")
        elif choice == "2":
            x, y = get_number("Enter first number: "), get_number("Enter second number: ")
            print(f"Result: {subtract(x, y)}")
        elif choice == "3":
            x, y = get_number("Enter first number: "), get_number("Enter second number: ")
            print(f"Result: {multiply(x, y)}")
        elif choice == "4":
            x, y = get_number("Enter first number: "), get_number("Enter second number: ")
            print(f"Result: {divide(x, y)}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()