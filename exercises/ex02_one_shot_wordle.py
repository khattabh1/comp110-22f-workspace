"""My attempt at a sucessful wordle"""

__author__ = "730449789"

secret_word = ("python")
user_guess = (input("What is your 6-letter guess?: "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
box: str = ""
while len(user_guess)!= 6: #at this point I want the program to understand that unless the user input is 6 letters, it should tell them that it's wrong and prompt them to try again
    user_guess = input("That is not a 6-letter word, try again: ")
i = 0 
while i < len(secret_word):
    if user_guess[i] == secret_word[i]:
        box += GREEN_BOX
    if user_guess[i] in secret_word and user_guess[i] != secret_word[i]:
        box += YELLOW_BOX
    if user_guess[i] not in secret_word:
        box += WHITE_BOX
    i = i + 1 #this is the end of the while loop, in this loop I asked the code to ask itself whether index variable i, is less than the length of the secret word, this would mean that the program would stay in the while loop for as long as the index variable is less than 7-characters. Inside the loop I asked it three if statements. 
print(box)
if user_guess != secret_word:
        print('Not quite, play again soon')
else:
    print('Woo! You got it')    



