#Chatbot Pearl

print("Hi there! My name is Pearl!")
print()

start=input("Do you want to interact with me(yes or no):")
print()

start=start.lower()

if start=="yes":
    mood=input("Wonderful! How are you feeling today(bored, sad, angry, scared, happy, excited, proud, or love:")
    print() 

    #mood=mood.title

    if mood=="bored":
        print("Why don't you make a craft, or another chatbot like me?")

    elif mood=="sad":
        why=input("I'm sorry to hear that.Why are you sad:")
        print()
        print("I'm sorry. :(")

    elif mood=="angry":
        calm=input("I'm sorry to hear that. What happened:")
        print()
        print("Just take a deep breath and work it out.")

    elif mood=="scared":
        scared=input("Im sorry to here that. What scared you:")
        print()
        print("Don't worry. Everything will be alright.")

    elif mood=="happy":
        print("It's nice to hear that you're in a good mood!")

    elif mood=="excited":
        print("Yay!")

    elif mood=="proud":
        proud=input("Yay! Why are you proud:")
        print("Well, I'm glad to hear that!")

    elif mood=="love":
        love=input("Who do you love:")
        print("I'm guessing love a such a beautiful feeling. But as a chatbot, I can't feel it...")


elif start=="no":
    (":( OK. If you change your mind you can always call me again.")

    

    
