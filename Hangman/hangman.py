import random

def print_scaffold(guesses, wd):
    if (guesses == 0):
        print ("_________")
        print ("|	 |")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
    elif (guesses == 1): 
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
    elif (guesses == 2):
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	 |")
        print ("|	 |")
        print ("|")
        print ("|________")
    elif (guesses == 3):
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|")
        print ("|	 |")
        print ("|")
        print ("|________")
    elif (guesses == 4):
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|/")
        print ("|	 |")
        print ("|")
        print ("|________")
    elif (guesses == 5):
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|/")
        print ("|	 |")
        print ("|	/ ")
        print ("|________")
    elif (guesses == 6):
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|/")
        print ("|	 |")
        print ("|	/ \ ")
        print ("|________")
        print("\n")
        print("The word was %s." %wd)
        print("\n")
        print("\nYOU LOSE!! TRY AGAIN!!")
        
        ans = str(input('Would you like to play again? (Y/N) '))
        if ans.lower() == 'y':
            hangman()
        quit()
        

def selectWord():
    file = open('WORD.txt')
    words = file.readlines()
    myword = 'a'
    while len(myword) < 4:
        myword = random.choice(words)
        myword = str(myword).strip('[]')
        myword = str(myword).strip("''")
        myword = str(myword).strip("\n")
        myword = str(myword).strip("\r")
    myword = myword.lower()
    return myword

def hangman():
    guesses = 0
    word = selectWord()
    word_list = list(word)
    blanks = "_"*len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []

    print("GAME START!\n")
    print_scaffold(guesses, word)
    print("\n")
    print(" + ' ".join(blanks_list))
    print("\n")
    print("Guess a letter.\n")

    while guesses < 6 :

        guess = str(input("> "))
        guess = guess.lower()

        if len(guess) > 1:
            print("Enter one letter at a time!")
        elif guess == "":
            print("Enter one letter at a time")
        elif guess in guess_list:
            print("You already guessed that letter. Here are what you have guessed:  ")
            print(" ".join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i += 1

            if new_blanks_list == blanks_list:
                print("Your letter isn't here.")
                guesses = guesses + 1
                print_scaffold(guesses, word)

                if guesses < 6:
                    print("Guess again.")
                    print(" ".join(blanks_list))
            elif word_list != blanks_list:
                blanks_list = new_blanks_list[:]
                print(" ".join(blanks_list))

                if word_list == blanks_list:
                    print("\nYOU WIN!")
                    print("\n")

                    ans = str(input('Would you like to play again? (Y/N) '))
                    if ans.lower() == 'y' :
                        hangman()
                    quit()

                else: 
                    print("Great guess! Guess another!")
hangman()