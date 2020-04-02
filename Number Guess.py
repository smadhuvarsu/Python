from random import randint
print("==================================================================")
print("============Welcome to Bay Area Maker Faire 2019==================")
print("==================================================================")
print("============Let's have some fun guessing the numbers!=============")
print("==================================================================")

cont="y"
game_count=0
guess_count=0
best_game=0 
guess=0
guesses_per_game=[]

while cont=="y":
    game_count+=1
    num=randint(1,101)
    print("Okay...I am thinking of a number from 1 to 100 ;) ")
    guess = -1
    while (guess != num):
        guess=int(input("=> Enter your guess:"))
        guess_count+=1
        if (guess < num):
            print("<<< You guessed too low! :( >>>")
        elif(guess > num):
            print("<<< You guessed too high! :( >>>")
        else:
            print("<<< Yay!You are correct!:) >>>")
            cont=input("=> Do you want to continue(y/n)?:")
            guesses_per_game.append(guess_count)
    
    
print("Okay!Thank you!")
print("Here are your results:")
print("Total games:" ,game_count)
print("Total guesses:" ,guess_count)
sum=0

for i in (guesses_per_game):
    sum+=1

print("Guesses per game:",round((float(guess_count)/float(game_count)), 2))

if (guess_count==1):
    best_game=1

for i in (guesses_per_game):
    if (best_game<i):
        best_game=i
print("Best game:" ,best_game,"guesses.")



'''
def rand_num():

    num=randint(1,100)
    print(num)

    print("I am thinking of a number from 1 to 100...")
    guess=int(input("Enter your first guess:"))
    if guess==(num):
        print("Yay!You are correct!")
        cont=input("Do you want to continue(y/n)?:")
        if guess != (num):
        '''
            















































    



    


    
        


 
