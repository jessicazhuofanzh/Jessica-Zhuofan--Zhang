
# Isolated Island
# Now updated to Python 3

# At the top of the file are declarations and variables we need.
# 
# Scroll to the bottom and look for the main() function, that is
# where the program logic starts.

import random # random numbers (https://docs.python.org/3.3/library/random.html)
import sys # system stuff for exiting (https://docs.python.org/3/library/sys.html)

# an object describing our player
player = { 
    "name": "p1", 
    "score": 0,
    "items" : ["milk"],
    "friends" : [],
    "location" : "start"
}

rooms = {
    "room1" : "an isolated island",
    "room2" : "a long path",
    "room3" : "a scary path"
}

def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print ("You roll a: " + str(result) + " out of " + str(maxNum))

    if (result <= difficulty):
        print ("trying again....")
        
        raw_input("press enter >")
        rollDice(minNum, maxNum, difficulty) # this is a recursive call

    return result

def printGraphic(name):
    if (name == "house"):
        print ('                 __- -                      ')
        print ('                (                           ')
        print ('               _))_                         ')
        print ('               |  |________                 ')
        print ('      .-------"""""   |    """""------.     ')
        print ('     /.".\            |            /.".\    ')
        print ('    /.   .\           |           /.   .\   ')
        print ('   /.     .\          |          /.     .\  ')
        print ('  /.  ___ '          "T"          ' ___  .\ ')
        print (' |   |_|_|  |   _..   |   --.   |  |_|_|  | ')
        print (' |   |_|_|  |  |  |   |   |_|   |  |_|_|  | ')
        print (' |__________|__|..+--"""--....__|_________| ')
        print ('               the house                    ')
    if (name == "man"):
        print ('            ))),,       ')
        print ('           /  ///       ')
        print (' .        . .  /        ')
        print (' \\      <     )        ')
        print (' -C\      \_- |         ')
        print (' \_/     __|__/L__      ')
        print ('        /         \     ')
        print ('             ___   \    ')
        print ('             \ /        ')
        print ('              V  __     ')
        print ('              |--\      ')
        print ('              \__/--    ')
        print ('         the man        ')

    if (name == "key"): 
        print ('     ,o.          8 8    ')
        print ('    d   bzzzzzzzza8o8b   ')
        print ('      `o                 ')
        print ('         the key         ')

    if (name == "ghost"):
        print ('      .````.      ...           ')
        print ('     :o  o `....``  ;           ')
        print ('     `. O         :`            ')
        print ('       ``:          `.          ')
        print ('         `:.          `.        ')
        print ('          : `.         `.       ')
        print ('         `..``...       `.      ')
        print ('                 `...     `.    ')
        print ('                     ``...  `.  ')
        print ('                          `````.')
        print ('                                ')
        print ('        not-so-scary ghost      ')

    if (name == "title"):
        print ('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
        print ('.            _.,.__       .                                   .')
        print ('.           ((o\o\))     .                                   . ')
        print ('.     .-.    `    ``      .    A tropical island              .')
        print ('.  __(   )___.o"^^".,___  .                                   .')
        print ('.     ===    ~~~~~~~~     .                                   .')
        print ('.      ==             ldb .                                   .')
        print ('.       =                 .                                   .')
        print ('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')



def gameOver():

    printGraphic("title")

    print("-------------------------------")
    print("to be continued!")
    print("name: " + player["name"] ) # customized with a name
    print( "score: " + str(player["score"]) ) # customized with a score
    return

def scaryPath():
    print("The path led you to a cave.")
    print("It's dark and you feel really scared...")
    print("Then you see there's something moving! It's a man!")
    printGraphic("man")
    raw_input("press enter >")

    print("You consider your options.")
    print("options: [ talk to the man , walk around , back to island]")

    pcmd = raw_input(">")

    if (pcmd == "talk to the man"): 
        print ("You walk to the man.")
        print ("Let's roll a dice to see what happens next!")

        # roll a dice from 0 to 20 to see what happens
        # if your number is higher than the difficulty, you win!
        difficulty = 10
        roll = rollDice(0, 20, difficulty)
        
        # you have to get lucky! this only happens to the player
        # if you roll the dice high enough
        if (roll >= difficulty):
            print ("The man say he has a boat which can help you escape from the island!")
            print ("Do you want to ask for the key?")
            
            printGraphic("key")

            # we dive further into the logic
            pcmd = raw_input("yes or no >")

            if (pcmd == "no"):
                print ("You leave it there.")
                scaryPath()

            elif (pcmd == "yes"):
                print ("You take the key and find the boat.")
                player["items"].append("gem") # add an item to the array with append
                player["score"] += 100 # add to the score
                isolatedIsland()

            else:
                print ("You leave it there.")
                isolatedIsland()

        else:
            print ("Turns out it's nothing... oh well.")
            scaryPath()

    elif (pcmd == "walk around"):
        print ("You walk around... you have a strange feeling")
        print ("that you never leave the cave...") # the lost woods reference
        scaryPath()

    elif (pcmd == "back to island"):
        print ("You decide to go back.")
        pcmd = raw_input(">")
        isolatedIsland()

    else:
        print ("You can't do that!")
        scaryPath()


def longPath():
    print ("The long path leads you down a narrow road.")
    print ("You see there is a big house at the end of the road.")
    raw_input("press enter >")

    printGraphic("house")
    print ("It looks like an abandoned house.")
    print ("You stand in front of the house.")
    print ("The door open...")
    raw_input("press enter >")
    
    print ("You consider your options.")

    # check the list for items
    # the 'in' keyword helps us do this easily
    if ("key" in player["items"]):
        print ("options: [ go back, enter the house, give up key, screaming ]")
    else:
        print ("options: [ go back, enter the house, run ]")

    pcmd = raw_input(">")

    # option 1: look at the fox
    if (pcmd == "go back"):
        print ("You go back...")
        isolatedIsland() # try again
    
    # option 2: enter the house
    elif (pcmd == "enter the house"):
        print ("You walk into the house")
        print ("Let's roll a dice to see what happens next!")
        raw_input("press enter to roll >")

        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            print ("It's some food! You're lucky.")
            player["score"] += 50
        else:
            print ("You walk around, but... you got lose.")
            longPath() # try again
        
        # nested actions and ifs
        pcmd = raw_input("You like the house, do you want to stay? yes or no >")

        # yes
        if (pcmd == "yes"):

            print ("You really like live in this house!")

            player["friends"].append("white fox")

            # string and int converstion!
            # we need to convert the score to a number to add to it
            # then convert it back to a string to display it to the player
            player["score"] = int(player["score"]) + 100 # conversion

            # we generate a custom string and add the score
            print ( "Your score increased to: " + str(player["score"]) ) 
            
            gameOver()

        # no
        elif (pcmd == "no"):
            print ("You walk back...")
            longPath()
        
        # try again
        else:
            longPath()

    elif (pcmd == "give up key"):
        print ("You throw away the key.")
        raw_input("press enter>")
        printGraphic("key")
        gameOver()

    # option 3: run
    elif (pcmd == "screaming"):
        print ("It's so scary!")
        isolatedIsland() # back to start

    # try again
    else:
        print ("I don't want to go in there.")
        longPath() # long path

def isolatedIsland():
    print ("You are in an isolated island.")
    print ("There is a path ahead of you and another path to the right.")
    
    # this piece of game logic checks to see if the requirements are met to continue.
    # we can have some fun and change the options for the player
    # based on variables we stored

    # 1. check the list of items, to see if it is there
    # 2. check the list of friends, to see if you are in friends list

    if (("key" in player["items"]) and not ("fox" in player["friends"])):
        print ("Your options: [ look around, path, trade key with the island ghost]")

    elif ("key" in player["items"]):
        print ("Your options: [ look around, path, exit ]")

    else:
        print ("Your options: [ look around, path , other path , exit ]")


    pcmd = raw_input(">") # user input

    # player options
    if (pcmd == "look around"):
        # its a trick!
        print ("You look around... you hear some scary moan")

        raw_input("press enter >")
        isolatedIsland()

    # path option
    elif (pcmd == "path"):
        print ("You take the path.")
        raw_input("press enter >")
        longPath() # path 1

    # path2 option
    elif (pcmd == "other path"):
        print ("You take the other path.")
        raw_input("press enter >")
        strangePath() # path 2

    # exiting / catching errors and crazy inputs
    elif (pcmd == "exit"):
        print ("you exit.")
        return # exit the application

    elif (pcmd == "trade key with the island ghost"):
        print ("you give the key to the ghost... hugh?")
        printGraphic("ghost")

        print ("'tooooodaaloooooo'\", he says.") # escaped
        return # exit the application, secret ending

    else:
        print ("I don't understand that")
        isolatedIsland() # the beginning
        

def introStory():
    # let's introduce them to our world
    print ("Nice to meet you! What should I call you?")
    player["name"] = raw_input("Please enter your name >")

    # intro story, quick and dirty (think star wars style)
    print ("Welcome to the isolated island " + player["name"] + "...")
    print ("The story so far...")
    print ("You wake up in the morning.")
    print ("You found that you are in a strange place...")
    print ("There's no body around you...")
    print ("Do you want to go check what's happening?")

    pcmd = raw_input("please choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print ("You walk out the room, you found out that you are in a isolated island...")
        raw_input("press enter >")
        isolatedIsland()
    else:
        print ("No? ... That doesn't work here.")
        pcmd = raw_input("press enter >")
        introStory() # repeat over and over until the player chooses yes!

# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens
