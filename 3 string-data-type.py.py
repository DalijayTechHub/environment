"""
Your module description
"""
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
name = input("What is your name? ")
print(name)
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))


output

This is a string.
<class 'str'>
This is a string. is of the data type <class 'str'>
waterfall
What is your name? James Ackah-Blay
James Ackah-Blay
What is your favorite color?  Gren
What is your favorite animal?  Catty
James Ackah-Blay, you like a Gren Catty!