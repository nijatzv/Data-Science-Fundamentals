
# lets create a robot translator where: all vowels will be replaced with "0"
# banana -> b0n0n0, wrestling -> wr0stl0ng
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():        # if added phrase starts with upper case, replacewith uppercase
                translation = translation + "C"
            else:
                translation = translation + "c"
            
            # if i have a vowel, replace them with 0
        else:
            translation = translation + letter  # if i dont have a vowel, add letter to translation
    return translation

print(translate(input("Add a phrase: ")))






