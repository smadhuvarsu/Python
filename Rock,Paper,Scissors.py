import random

moves=["r","p","s"]
cscore=0
uscore=0
tscore=0

name=input("What is your name:")
print()
print("Hi",name.title(),"! Are you ready to play rock,paper scissors? Good! If you want to do rock,enter 'r'.If you want to do paper,enter 'p'.If you want to do scissors,enter 's'.Your oppenent will be the computer.")
print()
rounds=int(input("One minute...please enter how many rounds you want to play:"))
print("-------------------------------------------------------------------------------------------------------------")

for i in range(rounds):
    print("Round #",i+1)
    user=input("What is your move:")
    computer=random.choice(moves)

    #Computer Wins
    if (computer=="s") and (user=="p"):
        print("Computer wins!")
        cscore+=1
    
    elif (computer=="r") and (user=="s"):
        print("Computer wins!")
        cscore+=1
    
    elif (computer=="p") and (user=="r"):
        print("Computer wins!")
        cscore+=1
    

    #User Wins
    elif (computer=="s") and (user=="r"):
        print("You win!")
        uscore+=1
    
    elif (computer=="r") and (user=="p"):
        print("You win!")
        uscore+=1
    
    elif (computer=="p") and (user=="s"):
        print("You win!")
        uscore+=1
    
    #Tie
    elif (computer=="r") and user=="r":
        print("It is a tie!")
        tscore+=1
    
    elif (computer=="p") and (user=="p"):
        print("It is a tie!")
        tscore+=1
    
    elif (computer=="s") and (user=="s"):
        print("It is a tie!")
        tscore+=1
        
    else:
        print("Something went wrong(I think you typed an unknown letter or a number).")
        print("This means you will have to miss a turn..:(")
        

print("Here are your scores:",uscore)
print("Here are the computer's scores:",cscore)
print("Here are the number of ties you had:",tscore)

if (cscore>uscore):
    print("The winner of this game is..the Computer!")

if (uscore>cscore):
    print("The winner of this game is..",name.title(),"!")

        
    


