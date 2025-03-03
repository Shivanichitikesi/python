#                   HANGMAN GAME BY SHIVANI CHITIKESI
import random
import time

# The parameters we require to execute the game:
def game():
    global word
    global count
    global chance
    global length
    global playgame
    global guessed
    global hangmanword
    word_to_guess=["january","border","image","film","promise","kids","lungs","doll","rhyme",
                   "damage","plants","apple", "banana", "cherry", "date", "elderberry","fig",
                   "grape", "honeydew", "kiwi", "lemon","mango", "nectarine", "orange","papaya",
                   "quince","raspberry", "strawberry", "tangerine", "ugli fruit", "watermelon"]
    word=random.choice(word_to_guess)
    length=len(word)
    hangmanword="-"*length
    count=0
    chance=5
    guessed=[]
    playgame=""
    hangman()

# A loop to re-execute the game when the first round ends:
def loopplay():
    global playgame
    playgame=input("Do want to play again y for yes & n for no:")
    playgame=playgame.strip()
    while playgame not in ['Y','N','y','n']:
        playgame=input("Do want to play again y for yes & n for no:")
        playgame=playgame.strip()
    if playgame=='y' or playgame=='Y':
        game()
    elif playgame=='n' or playgame=='N':
        exit()

# Initializing all the conditions required for the game:
def hangman():

    global word
    global count
    global chance
    global length
    global guessed
    global playgame
    global hangmanword
    
    guess=input("This is Hangman word:"+hangmanword+ " Enter your guess:")
    guess=guess.strip()
    

    if len(guess)==0 or len(guess)>1 or guess<="9":
        print("Invalid input! Lets Try Again")
        hangman()
    
    elif guess in word:
        guessed.extend([guess])
        index=word.find(guess)
        word=word[:index]+'-'+word[index+1:]
        hangmanword=hangmanword[:index]+guess+hangmanword[index+1:]
        print(hangmanword+"\n")

    elif guess in guessed:
        print("Try another letter\n")

    else:
        count+=1
        chance-=1

        if count==1:
            time.sleep(1)
            print("   ______\n"
                  "  |      \n"
                  "  |      \n"  
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |        \n"
                  "__|__      \n")
            
            print("\nWrong choice. You have "+str(chance)+ "guesses left")
        elif count==2:
            time.sleep(1)
            print("   ______\n"
                  "  |      |\n"
                  "  |      |\n"  
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |        \n"
                  "__|__      \n")
            
            print("\nWrong choice. You have "+str(chance)+ "guesses left")   

        elif count==3:
            time.sleep(1)
            print("   ______\n"
                  "  |      |\n"
                  "  |      |\n"  
                  "  |      O \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__      \n")
            
            print("\nWrong choice. You have "+str(chance)+ "guesses left")   
            
        elif count==4:
            time.sleep(1)
            print("   ______\n"
                  "  |      |\n"
                  "  |      |\n"  
                  "  |      O \n"
                  "  |     /|\ \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__      \n")
            
            print("\nWrong choice. You have "+str(chance)+ "guesses left")   

        elif count==5:
            time.sleep(1)
            print("   ______\n"
                  "  |      |\n"
                  "  |      |\n"  
                  "  |      O\n"
                  "  |     /|\ \n"
                  "  |     /|\ \n"
                  "  |       \n"
                  "  |        \n"
                  "__|__      \n")
            
            print("\nWrong choice. You are HANGED !!") 
            print("The word was:",guessed,word)
            loopplay()

    if word =="-"*length:
        print("Correct Guess!\n")
        print(f"\t\t\tYou Won! Congrants {name}\n")
        loopplay()
    elif count!=chance:
        hangman()

# Initial Steps to invite in the game:
print("\n\n\t\t\t\t\tWELCOME TO HANGMAN GAME BY SHIVANI CHITIKESI\n\n")
time.sleep(2)
name=input("\nEnter your name:")
print(f"\nHowdy {name}! Best of Luck\n")
print("The game is about to start")
time.sleep(2)
print("Lets Play!\n")

game()