import random

# List of words
wordbank = ["jellyfish", "telephone", "universal", "copyright", "palindrome", "superhuman", "Pokemon", "incredible", "starstruck", "soccer", "hockey", "basketball", "football", "softball", "swimming,",
"track", "curling", "calgary", "toronto", "mississauga", "saskatoon", "vancouver", "edmonton",
"ottawa", "winnipeg", "canada", "italy", "argentina", "germany", "egypt", "finland"]
 
# List of the hangman drawing parts
drawing = ["|--------", "|    O ", "| ---|---", "|   / \ ", "|  /   \  ", "|________"]
 
y = 0

# The program will loop until the user presses quit
while y == 0:

    # Checks to see if there are words left in the wordbank
    if len(wordbank) == 0:
        print("OH SNAP, NO WORDS LEFT!")
        print("System off!")
        y = 1
        break

    else:
        pass
    # Generates a random index of the list of words
    ranword = random.randint(0, len(wordbank) - 1)  

    # Random word is chosen
    word = wordbank[ranword]
    
    # Made so the words don't repeat
    wordbank.pop(ranword)

    blank = ""
    new = []
    misses = ""
    guesses = []
    
    # Add a blank to both the list and string for every index in the secret word
    for counter in range(len(word)):
       blank += "_"
       new.append("_")
 
    print("Word: ", blank)
    
    # This will loop until the game is over
    while True:
      
        print("Misses: ", misses)
        guess = input("Guess: ")
        
        # Adds the guess a list
        guesses.append(guess)
        newword = ""
        index = 0
        miss = True
    
        # Cycles through the indices
        while index < len(word):
            
            # if the guess is the same as one of the letters in the secret word...
            if guess.lower() == word[index]:
                
                # It will remove the blank space at the index
                new.pop(index)

                # The guess is then substitued instead of the blank
                new.insert(index, guess.lower())
                
                # It is not a miss
                miss = False

            else:
                pass
                
            index += 1

            n = 0

            # Cycles through the guesses
            while n < len(guesses) - 1:
                
                # If the guess exists or is empty then the count is subtracted by 1 which means it won't add to the misses and the loop it just asks for another guess
                if guess == guesses[n] or guess == "":
                    miss = False
                    break

                else:
                    pass

                n += 1
    
            # Check to see if the count is the same as the index 
        if miss == True:

            # if it is then it adds the guess to the misses
            misses += guess.lower()
    
        else:
            pass
        
            # turns the list into a string which will be displayed and with every guess
        for counter in range(len(new)):
            newword += new[counter]
    
            # checks to see if the number of misses is the same as the lenth of the drawing list
        if len(misses) == len(drawing):

            # if it is then the game is over
            print("------------------")
            print("THE STICK MAN IS DEAD! YOU LOSE!")
            print("The word was", word)
            print("------------------")
    
                # Asks the user if they want to play again
            again = input("Enter Q to quit (Tap anything else to play again): ")
    
                # if not, y = 1 ending the big while statement and it breaks the guessing while statement
            if again.upper() == "Q":
                print("------------------")
                print("Thanks for playing!")
                print("System Off")
                y = 1
                break
    
                # if yes then the game is reset
            else:
                print("------------------")
                break
            
        # The rest is more ways the user can win or lose and is follows similar steps

        x = 0
    
        while x <= len(misses):
            print(drawing[x])
            x += 1
            
        
        if guess.lower() == word:
            
            print("------------------")
            print("Word: ", word)
            print("Misses: ", misses)
            print("------------------")
            print("YOU WIN!")
            print("------------------")
    
            again = input("Enter Q to quit (Tap anything else to play again): ")
    
            if again.upper() == "Q":
                print("------------------")
                print("Thanks for playing!")
                print("System Off")
                y = 1
                break
    
            else:
                print("------------------")
                break
    
        elif newword == word:
            
            print("------------------")
            print("Word: ", word)
            print("Misses: ", misses)
            print("------------------")
            print("YOU WIN!")
            print("------------------")
    
            again = input("Enter Q to quit (Tap anything else to play again): ")
    
            if again.upper() == "Q":
                print("------------------")
                print("Thanks for playing!")
                print("System Off")
                y = 1
                break
    
            else:
                print("------------------")
                break
    
        else:
            print("------------------")
            print("Word: ", newword)
