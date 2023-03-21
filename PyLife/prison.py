import random as r
import time

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
                        turn = False
        return inPrison




        



#class Riot: