# Create a program that will --

# Check if the given number is a palindrome number.

# DEADLINE: JANUARY 26, 2024

# pseudocode

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers
# Expected results:

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

# Asking the user to input a number
given_number = int(input("Enter a number: "))
print("The original number is:", given_number)

# Converting the given number from integer to string
given_number_str = str(given_number)[::-1]

# Setting up a variable
reverse_number = int(given_number_str)

# Checking if the given number is Palindrome number using if else statement
if given_number == reverse_number:
    print("The given number is a Palindrome number")
else:
    print("The given number is not a Palindrome number")