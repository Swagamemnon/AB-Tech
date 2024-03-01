# prompt user to input number
number = input("Enter any number and I'll tell you if it's divisible by 10: ")

# convert user input string to integer
number = int(number)

# determine whether number is a multiple of 10 and print result
if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10!")
else:
    print(f"\nThe number {number} is not a multiple of 10")