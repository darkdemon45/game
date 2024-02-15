

def v():   
    def g():
        print("Do you want to quit")
        print("1.Yes/2.Start a new game")
        h=int(input("1/2-"))
        if(h==1):
            print("!!you quit!!")
        elif(h==2):
            v()
     
    print(" Hi, welcome to this jungle game.")
    print("1. Now you are in the jungle.")
    print("2. You went too deep in the jungle.")
    print ("Now you lost in the jungle, you need to find a way to out 1.left 2.Right 3. for quit.")

    a=int(input("select one way"))
    if(a==1):
        print(" You are in left way.")
        print("1. You feel hungry.")
        print("2. Now you hear a noice.")
        b=int(input("Press1 for ignore the voice/press2 for search where the voice come from/3 for quit.="))
        if(b==1):
            print("You lost somewhere in jungle.")
            print("You died because you eat poisonous mushroom (death cap).")
            print("!!!GAME OVER!!!")
            g()
        elif(b==2):
            print(" You found a guy.")
            print("1 And he offer you some food.")
            print("2 And he shows the way to out.")
            print("Trust him press1/don't trust him press2/3 for quit")
            f=int(input("1/2/3--"))
            if(f==1):
                print("You trust him and take that way.")
                print("Soon a group of wolves attacked you.")
                print("!!!YOU DIED!!!")
                g()
            elif(f==2):
                print("1. You didnt trust him and choose anther way.")
                print("2. Soon you found a cave.")
                print("Rest in cave press1/press2 to leave.") 
                s=int(input("1/2--"))
                if(s==1):
                    print("a bear found you and kill you.")
                    print("!!!you lose!!!")
                    g()
                elif(s==2):
                    print("You run from there.")
                    print("Soon you slip from mountain and you died.")
                    print("!!!YOU DIED!!!")
                    g()
                else:
                    print("enter a valid number.")
            elif(f==3):
                g()
            else:
                print("enter a valid number.") 
        elif(b==3):
            g()
        else:
            print("enter a valid number.")                   
    elif(a==2):
        print("You are in right way.")
        print("1. You hear a noice.")
        print("2. You want to follow that voice-press1-to follow,press2- to ignore")
        c=int(input("enter a value"))
        if(c==1):
            print("You found a dead man with gun.")
            print("1. You pick that gun and found some food and ammo in his bag.")
            print("2. Soon you hear a tiger roar.climb a tree-press1/ run-press2/3 for Quit")
            e=int(input("1/2/3="))
            if(e==1):
                print("Now you climbed a tree and satdown.")
                print("Now you load your gun.")
                print("Now you point your gun to the tiger.")
                print("Now you fire a bullet and kill a tiger.")
                print("Someone hear a gunshot and came to you,and save yourlife.")
                print ("!!!you won!!!")
                g()
            elif(e==2):
                print("Tiget saw you running,tiger starts follows you.")
                print("Soon tiger caught you and kill you.")
                print("!!!you killed by tiger!!!,you lose.")
                g()
            elif(e==3):
                g()
            else:
                print("enter a valid number")    
        elif(c==2):
            print("You igmore that voice and you found a river.")
            print("1. You jump in thr river and you cross the river.")
            print("2. After some time you feel so weak and dizzyness soon you found leeches in your body.")  
            print ("You found smoke.find where it come from press1/press2 to ignore and take some rest/3 Quit")
            d=int(input("press1/press2-"))
            if(d==1):
                print("You found a tribe.")
                print("Tribe helps you to get rid from leeches.")
                print("They offer you food and now you are well.")
                print("They shows you a way to outside the jungle.")
                print("You follow the path and you found the exit.")
                print("!!! WE HAVE A WINNER !!!")
                g()
            elif(d==2):
                print("Now you are too weak.")
                print("A crockdile eat you.")
                print("!!!YOU DIED!!!")
                print("!!!GAME OVER!!!")
                g()
            elif(d==3):
                g()
            else:
                print("enter a valid number")
        elif(c==3):
            g()    
        else:
            print("enter a valid number")
    elif(a==3):
        g()
    else:
        print("enter a valid number")

v()


