def get_day_of_week(number):
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days_of_week[number % 7]

def main():
    while True:
        try:
            number = int(input("Enter a number to determine the day of the week "))
            day = get_day_of_week(number)
            print(f"The day corresponding to {number} is {day}.")
        except ValueError:
            print("Invalid input. Please enter a valid number. ")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()