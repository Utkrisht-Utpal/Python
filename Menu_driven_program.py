import math

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def check_positive_negative(number):
    if number > 0:
        return f"{number} is positive."
    elif number < 0:
        return f"{number} is negative."
    else:
        return f"{number} is zero."

def print_square(number):
    return f"The square of {number} is {number ** 2}."

def print_square_root(number):
    if number >= 0:
        return f"The square root of {number} is {math.sqrt(number)}."
    else:
        return "Square root of a negative number is not defined in real numbers."

def main():
    while True:
        print("\nMenu:")
        print("a) Check if the number is even or odd")
        print("b) Check if the number is positive or negative")
        print("c) Print the square of the number")
        print("d) Print the square root of the number")
        print("e) Exit")
        choice = input("Enter your choice (a/b/c/d/e): ").lower()

        if choice == 'e':
            print("Exiting the program.")
            break

        try:
            number = float(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 'a':
            print(check_even_odd(number))
        elif choice == 'b':
            print(check_positive_negative(number))
        elif choice == 'c':
            print(print_square(number))
        elif choice == 'd':
            print(print_square_root(number))
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
