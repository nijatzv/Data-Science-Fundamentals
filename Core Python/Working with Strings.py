# Strings are just plain Text

print("we can write whatever text we want")
print("we can write \nwhatever text we want")
print("we can write whatever\" text we want")

phrase = "Text we want"
print(phrase)
print(phrase + " is cool") #concaneation

# some string functions
print(phrase.lower())       # lowercase to the string
print(phrase.upper())       # uppercase to the string
print(phrase.isupper())     # checks if string is in uppercase or lowercase
print(len(phrase))          # length of the string
print(phrase[3])            # gives the character in location (4th place in here)
print(phrase.index("we"))   # finds the location of the character in string
print(phrase.replace("we", "you"))  # replaces the 1st with the 2nd word