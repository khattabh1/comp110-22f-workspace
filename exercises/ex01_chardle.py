"""Ex01 - Chardle - first real coding assignment"""

__author__ = "730449789"

word: str = input("Enter 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1: 
    print("Error: Character must be a single character.")
    exit()
instances: int = 0
print("Searching for " + letter + " in " + word)
if word[0] == letter:
    print(letter + " found at index 0")
    instances = instances + 1 
if word[1] == letter:
    print(letter + " found at index 1") 
    instances = instances + 1
if word[2] == letter:
    print(letter + " found at index 2")
    instances = instances + 1
if word[3] == letter:
    print(letter + " found at index 3")
    instances = instances + 1
if word[4] == letter:
    print(letter + " found at index 4")  
    instances = instances + 1      

if instances > 1:
    print(instances, "Instances of," ,letter, "found in", word)
elif instances == 1:
    print (instances, "Instances of, ",letter, "found in", word)
elif instances < 1:
    print(instances, "Instances of,",letter, "found in", word) 
else:
    print("No instances of " + letter + " found in " + word)
    exit()   

