import random
import getpass

#welcome message
print("HANGEMAN GAME")
counter = 0
while counter == 0:
    container=input("\nReady to play? (Yes?No)\n -> ")
    if container.lower()=="yes": 
        name_1=input("\nPlayer 1 enter your name : ")
        name_2=input("\nPlayer 2 enter your name : ")
        print("\n Let's Go.........")
        print (f"\n---------- {name_1} VS {name_2} -----------")
        print("")
        word= getpass.getpass(f"{name_1}, you are required to input a word (The word wont be visible on the screen so that your opponent doesn't see it ) :\n -> ")
        clue=input(f"{name_1}, input a clue to the word you entered: ")
        
        """for i in range(6):
            user_list = []
            user_input = input(f"{name_1}, enter value {i+1}: ")
            user_list.append(user_input)
            # Choose a random word from the list
            word = random.choice(user_list)"""
        #Create a list to store the guessed letters
        guessed_letters = ["_"] * len(word)
        # Create a variable to store the number of lives
        lives = 6
        print(f"\n\n{name_2} You have", lives, "lives.")

        while lives > 0:
            #print the current state of the word 
            print(" ".join(guessed_letters))

            #Ask the user for a guess
            guess=input("Guess a letter: ")

            # Check if the guess is in the word
            if guess in word:
                # Reveal the correct letter
                for i in range(len(word)):
                    if word[i] == guess:
                        guessed_letters[i] = guess
            else:
                # Decrease the number of lives
                lives -= 1
                print("Incorrect! You have", lives, "lives left.\n")

            # Check if the user has won
            if "_" not in guessed_letters:
                print("\nYou are correct the word is", word)
                print("Congratulations! You won! ")
               
                break
        

        if lives == 0:
            print("\nGame over! The word was", word)

    elif container.lower()=="no":
            exit=input("Are you sure you want to exist this game (yes?no)\n ->")
            match exit.lower():
                case "no" :
                    #code to run  
                    print("")
                    
                case "yes":
                    print("successfully exited game.") 
                    
    else:
      user_exit=input("You are to input (yes or no )")
      container.lower()=="no"    
      print("")
    #do for single and multiple player