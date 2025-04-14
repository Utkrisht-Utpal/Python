def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif 80 <= percentage < 90:
        return 'A'
    elif 70 <= percentage < 80:
        return 'B+'
    elif 60 <= percentage < 70:
        return 'B'
    elif 40 <= percentage < 60:
        return 'C'
    else:
        return 'FAIL'

def get_student_data():
    while True:
        try:
            physics = float(input("Enter marks obtained in Physics: "))
            chemistry = float(input("Enter marks obtained in Chemistry: "))
            mathematics = float(input("Enter marks obtained in Mathematics: "))

            if 0 <= physics <= 100 and 0 <= chemistry <= 100 and 0 <= mathematics <= 100:
                return physics, chemistry, mathematics
            else:
                print("Marks should be between 0 and 100. Please re-enter the marks.")
        except ValueError:
            print("Invalid input. Please enter numerical values for marks.")

def main():
    physics, chemistry, mathematics = get_student_data()

    total_marks = physics + chemistry + mathematics
    percentage = (total_marks / 300) * 100
    grade = calculate_grade(percentage)

    print(f"\nTotal Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()