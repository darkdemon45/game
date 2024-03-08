import random 
def quit():
        print("Do you want to quit")
        print("1.Yes/2.Start a new game")
        h=int(input("1/2-"))
        if(h==1):
            print("!!you quit!!")
        elif(h==2):
            game()
    
def game():
    def user_input():
        a=int(input("1 for stone , 2 for scissior, 3 for paper, 4 for QUIT!"))
        return a
    user=user_input()
    
#COMPUTER 
    d=[1,2,3]
    computer=(random.choice(d))
    print("value of computer is ",computer)

    if(user==computer):
        print("clash the game")
        game()
    elif(user==1 and computer ==3):
        print(f"computer wins as computer is {computer}")
        game() 
    elif(user==2 and computer ==1):
        print(f"computer wins as computer is {computer}")
        game()
    elif(user==3 and computer ==1):
        print(f"user wins as computer is {computer}")
        game()
    elif(user==1 and computer ==2):
        print(f"user wins{computer}")
        game()
    elif(user==2 and computer==3):
        print(f"user wins{computer}")
        game()
    elif(user==3 and computer==2):
        print(f"computer wins {computer}")
        game()
    elif(user==4):
        print("Are you sure to Quit game") 
        quit()   
    else:
        print("wrong input kindly enter between 1,2,3")
        game()
game()
