age = int(input("Please enter your correct age: "))

if age > 39 and age < 65:
    print("You're over the hill.")
elif age > 100:
    print("sorry you are dead.")
elif age >= 64:
    print("Enjoy your retirement")
elif age <= 13:
    print("You qualify for a kiddie discount")
elif age == 21:
    print("Congrats on your 21st")
else:
    print("Age is but a number")