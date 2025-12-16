def checkAge():
    while True:
        try:
            age = int(input('Enter your age: '))

            if (age <= 18):
                print('You are a minor!')
            elif(18 < age <= 60):
                print("You are a major!")
            else:
                print("You are a senior citizen...")
            
            break
        except ValueError:
            print("You are dead!! 💀")
checkAge()