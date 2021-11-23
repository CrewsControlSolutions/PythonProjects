# 
# Python: _._._
# 
# Author: Kyle Crews
# 
# Purpose: A demonstration of how to pass variables from function to function for a game.

def start(nice=0,mean=0,name=""):
    # get user's name
    name = describeGame(name)
    nice,mean,name = niceMean(nice,mean,name)

def describeGame(name):
    """check whether this is a new game. If it is, get the user's name. If not, thank the player for playing again and continue with the game"""
    # in other words, if we do not already have this user's name, then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        go = True
        while go:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean.")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    go = False
    return name

def niceMean(nice,mean,name):
    go = True
    while go:
        showScore(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice+1)
            go = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            go = False
    score(nice,mean,name) #pass the 3 variables to the score()

def showScore(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passed the values stored with the 3 variables
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        niceMean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way.".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone.".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    go = True
    while go:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            go = False
            reset(nice,mean,name)
        if choice == 'n':
            print("\nOh, so sad, we'll see you next time.")
            go = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice=0
    mean=0
    #notice, I do not reset the name variable as that sume user has elected to play again
    start(nice,mean,name)





if __name__ == "__main__":
    start()
