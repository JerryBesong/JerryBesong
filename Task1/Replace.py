word = ("The!quick!brown!fox!jumps!over!the!lazy!dog.")
print(word)

new_word = word.replace("!", " ")
print(new_word)

new_word2 = new_word.upper()
print(new_word2)


# i think the best way to reverse a string is by spliting it.
#        0123456789---------------------------------44 letters
word = ("The!quick!brown!fox!jumps!over!the!lazy!dog.")

new_word3 = new_word2[: : -1]
print(new_word3)

#slicing is a very key element in coding as it gives you the oppurtunity to access individual letters in a string

new_word4 = new_word2[:6:-5]
print(new_word4)