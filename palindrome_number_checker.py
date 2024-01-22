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
given_number = (input("Enter a number: "))
print("The original number is:", given_number)

# Using reverse function to reverse the given number 
given_number_str = str(given_number)
reverse_number = reversed(given_number_str)

# Checking if the given number is Palindrome number
if given_number_str == reverse_number:
    print("The given number is a Palindrome number")
else:
    print("The given number is not a Palindrome number")