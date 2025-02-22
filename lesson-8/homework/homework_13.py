try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input('Enter the second number: '))

    print(first_number / second_number)
except ValueError:
    print('You have not entered number.')
except ZeroDivisionError:
    print('You cannot divide by 0')
finally:
    print('Execution completed.')
