def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Division by zero is not allowed."

def main():
    while True:
        print("\nMenu:")
        print("1) Addition")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Division")
        print("5) Modulo")
        print("6) Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '6':
            print("Exiting the program.")
            break
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        
        if choice == '1':
            print(f"The result of addition is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of subtraction is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of multiplication is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result of division is: {divide(num1, num2)}")
        elif choice == '5':
            print(f"The result of modulo is: {modulo(num1, num2)}")
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()