
secret_word = "banana"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("you win!")

# lets make a limit for guessing
secret_word = "banana"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
# there are 2 possible ways that the loop will end
# 1 - guess = scret word; 2 - user out_of_guesses
if out_of_guesses:
    print('Out of guesses, you lose!')
else:
    print("you win")

