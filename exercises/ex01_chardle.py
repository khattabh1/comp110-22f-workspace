"""Ex01 - Chardle - first real coding assignment"""

__author__ = "730449789"

word: str = input("Enter 5-character word: ")
letter: str = input("Enter a single character: ")
print("Searching for " + letter + " in " + word)
if word[0] == letter:
    print(letter + " found at index 0")
elif word[1] == letter:
    print(letter + " found at index 1") 
elif word[2] == letter:
    print(letter + " found at index 2")
elif word[3] == letter:
    print(letter + " found at index 3")
elif word[4] == letter:
    print(letter + " found at index 4")        
else:
    print("No instances of " + letter + " found in " + word)

if len(letter) != 1: 
    print("Error: Character must be a single character.")

