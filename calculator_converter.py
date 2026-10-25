
def calculator():
    print("\n--- Calculator ---")
    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                print("Error: Cannot divide by zero.")
                return
            result = a / b
        else:
            print("Invalid operator.")
            return

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers.")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")

    try:
        choice = int(input("Choose conversion (1-6): "))
        value = float(input("Enter value: "))

        if choice == 1:
            result = value * 0.621371
        elif choice == 2:
            result = value / 0.621371
        elif choice == 3:
            result = (value * 9 / 5) + 32
        elif choice == 4:
            result = (value - 32) * 5 / 9
        elif choice == 5:
            result = value * 2.20462
        elif choice == 6:
            result = value / 2.20462
        else:
            print("Invalid choice.")
            return

        print("Converted value:", round(result, 2))

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== Interactive Calculator & Unit Converter =====")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
