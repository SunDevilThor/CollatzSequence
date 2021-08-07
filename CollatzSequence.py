def collatz():
    #number = int(input("Enter number: "))

    try:
        number = int(input("Enter number: "))

        while True:
            if number == 1:
                break

            elif number % 2 == 0:
                number = number // 2
                print(number)

            elif number % 2 == 1:
                number = 3 * number + 1
                print(number)

    except:
        print("Enter in a valid number")


collatz()

'''
number = int(input("Enter number: "))

while True:
    if number == 1:
        break

    elif number % 2 == 0:
        number = number // 2
        print(number)

    elif number % 2 == 1:
        number = 3 * number + 1
        print(number)
'''
