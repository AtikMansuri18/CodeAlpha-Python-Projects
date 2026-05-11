'''
✅ TASK 1: Hangman Game
Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time.
Simplified Scope:
● Use a small list of 5 predefined words (no need to use a file or API).
● Limit incorrect guesses to 6.
● Basic console input/output — no graphics or audio.
Key Concepts Used: random, while loop, if-else, strings, lists.

'''

import random #this is random library of python. 

print(" Hangman Game 🎮 ")

#dec=Dictionary to store randome name in key and Value Pairs 
dec={	
	"Nike": "Clothe Brand",
    	"Sony": "TV Brand",
    	"Fuse": "Chocolate Brand",
    	"Apple": "Fruit",
    	"Chess": "2 Player Game",
    	"Dog": "Animal"
}

#Define variable take rendom.
word=random.choice(list(dec.keys()))

#to give Hint so we Use one varible with Dictionary word
print("Hint :- ",dec[word])

g=[]#for guessed The word to Store here

c=6 #guessed Word Chance

#now this is main logic of game with while loops and conditions.

while c > 0:

	display=" "#define disply varible with empty String

	#now Show the Guessed latters with for loop
	#l is stand for  latter
	for l in word: 
		
		if l.lower() in g:	
			display +=	l + " "

		else:
			display += "_"

	print("\nword :- ",display)

#Now We check The Win Or Loose with If-else Condition

	if "_" not in display:
		print("You win 🎉")
		break 

#Take Value From User define Varabile gusse 
	guess=input("Enter a Latter :- ").lower()

# Check only one letter	
	if len(guess) != 1:
		print("Enter Only One Letter :- ")
		continue

	#Store guess word
	g.append(guess)

	#Wrong guess Logic
	if guess not in word.lower():
	        c -= 1
	        print("Wrong Guess ❌ :- ")
	        print("Chance Left:", c)

#No chance Logic
if c == 0:
	print("\nGame Over :- ")
	print("Correct Word:", word)
