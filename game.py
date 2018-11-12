secret_Word = "bulldog"
guess_Limit = 3
guess_Count = 0
guess = ""
out_of_guesses = False

while guess != secret_Word and not (out_of_guesses):
    if guess_Count < guess_Limit:
        guess = input("Enter your guess: ")
        guess_Count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You lose")
else:
    print("You Won!!")
