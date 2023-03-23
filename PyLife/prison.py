import random as r
import time
from npc import *

class Escape:
    #there will be several different minigames that are stored in this class to make stuff simple
    def BlackJack():
        value = r.randint(2,19)
        value_AI = r.randint(2,19)
        print("TO ESCAPE PLAY (scuffed) BLACKJACK")
        print("STARTING VALUE: "+str(value))
        print("OPPONANTS VALUE: " +str(value_AI))
        play = True
        while play:
            move = input("HIT OR STAND? H or S\n")
            if move.lower() == "h":
                value = value + r.randint(1,12)
                print("Value: "+str(value))
                if value > 21:
                    play = False
                    inPrison = True
                    print("You got caught trying to escape!")
                
                elif value == 21:
                    print("YOU WIN!")
                    play = False
                    inPrison = False
                    turn = True
                else:
                    print("THE OPPONANT HITS")
                    value_AI = value_AI + r.randint(1,12)
                    print("OPPONANT VALUE: "+str(value_AI))
                    if value_AI > 21:
                        print("You win")
                        inPrison = False
                        turn = False
                        play = False
                    if value_AI == 21:
                        print("you LOSE")
                        inPrison = True
                        turn = False
                        play = False
                    else:
                        turn = False
                
            elif move.lower() == "s":
                turn = True
                while value_AI < 21 and play == True and turn == True:
                    print("THE OPPONANT HITS")
                    value_AI = value_AI + r.randint(1,12)
                    print("OPPONANT VALUE: "+str(value_AI))
                    if value_AI > 21:
                        print("You win")
                        inPrison = False
                        turn = False
                        play = False
                    if value_AI == 21:
                        print("you LOSE")
                        inPrison = True
                        turn = False
                        play = False
                    else:
                        turn = True
        return inPrison




        



class Riot:
    def rally():
        characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        print("Rally everyone up to begin!!!")
        print("Enter the following characters...")
        rallySize = r.randint(2,11)
        totalRallied = 0
        x=1
        while x <= rallySize:
            char = r.choice(characters)
            enter = input("Enter this character: "+char+"\n")
            if enter != char:
                print("Incorrect button pressed")
            
            if enter == char:
                print("Correct button pressed")
                totalRallied = totalRallied + r.randint(1,3)
            x = x+1

        print("You rallied: " +str(totalRallied)+" inmates")
        return totalRallied
 
    #CREATE THE INMATE NPC
    def inmateNPC_Health():
        health = NPC.health()
        return health
    def inmateNPC_Smarts():
        smarts = NPC.smarts()
        return smarts
    
    #CREATE THE GUARD NPC
    def guardNPC_Health():
        health = NPC.health()
        return health

    def guardNPC_Smarts():
        smarts = NPC.smarts()
        return smarts

    def fight(inmateNPC_health,inmateNPC_smarts, guardNPC_health, guardNPC_smarts):
        inmatePoints = 0
        guardPoints = 0
        if inmateNPC_health > guardNPC_health:
            inmatePoints = inmatePoints+1
        if inmateNPC_smarts > guardNPC_smarts:
            inmatePoints = inmatePoints+1
        if guardNPC_health > inmateNPC_health:
            guardPoints = guardPoints+1
        if guardNPC_smarts > inmateNPC_smarts:
            guardPoints = guardPoints+1

        if inmatePoints > guardPoints:
            print("Inmates beat the guards, you attempt to escape")
            escape = r.randint(1,100)
            if escape > 60:
                print("you're free")
                inPrison = False
            else:
                print("you tried but failed")
                inPrison = True

        if guardPoints > inmatePoints:
            print("you were all beaten")
            inPrison = True
            
        if guardPoints == inmatePoints:

            inPrison = True
            print("You were all evenly matched - nothing happened")
        return inPrison
    

class Bail:
    def fee(sentence):
        bailFee = 0
        for i in range(1,sentence):
            bailFee = bailFee + 1000
        return bailFee