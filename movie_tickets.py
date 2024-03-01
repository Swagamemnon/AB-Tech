# prompt ussers to enter their age
age = input("Please enter your age: ")
age = int(age)
price_total = 0

# construct loop informing users of appropriate ticket price
if age < 3:
    print("Your ticket is free!")
elif age < 13:
    print("Your ticket is $10")
    price_total += 10
else:
    print("Your ticket is $15")
    price_total += 15
print(f"\nYour total price is ${price_total}")