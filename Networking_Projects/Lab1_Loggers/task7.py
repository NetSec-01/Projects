class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass

number = 10

while True:
    try:
        guess = int(input("Enter a number: "))
        if guess == number:
            break
        elif guess < number:
            raise ValueTooSmallError
        elif guess > number:
            raise ValueTooLargeError
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too laarge, try again!")
        print()

print(ValueTooSmallError)
print("Congratulations! You gussed it correctly.")


