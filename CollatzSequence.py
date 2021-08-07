# CollatzSequence
# Objective: When entering in any number, the Collatz Sequence will evaluate down to 1.

def collatz():

    try:
        number = int(input("Enter number: "))

        while True:
            if number == 1 or number == 0:
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
