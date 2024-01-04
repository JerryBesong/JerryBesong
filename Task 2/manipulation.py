print()
print("Hello there? " )
print()
user_sent = input("Can you please help me insert a sentence here? ")
print()
print("Got the sentence, Thank You")

str_manip = user_sent
print()
lenght_of_strin = len(str_manip)

print("after counting the letters in your sentence i got this")
print()
print("total letters " + str(lenght_of_strin))
print()

print("i will like to change the alphabet (e) on your sentence to (@) if you dont mind" )
print()
new_strin = str_manip.replace("e", "@")
print(new_strin)

print()
print("also, let me invert the last letters of your sentence")
print()
new_strin2 = str_manip[-1:-4:-1]
print(new_strin2)
print()
print("Finally i craeted a word from your first three letters and your last two lettrs of your sentence")
new_strin3 = str_manip[:3:1]
new_strin4 = str_manip[-1:-2:-1]
print()
print(new_strin3 + new_strin4)
print()
print("THANK YOU")
print()
