
def calculate(choice):
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Addition =", a + b)
    elif choice == 2:
        print("Subtraction =", a - b)
    elif choice == 3:
        print("Multiplication =", a * b)
    elif choice == 4:
        if b != 0:
            print("Division =", a / b)
        else:
            print("Division by zero is not possible.")
    else:
        print("Invalid choice!")


print("----- MENU -----")
print("1. Perform addition")
print("2. Perform subtraction")
print("3. Perform multiplication")
print("4. Perform division")

ch = int(input("Enter your choice (1-4): "))

calculate(ch)
