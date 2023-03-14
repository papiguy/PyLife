import random
import time
#import each quadrant of the game here
from player import Player
from activities import *
from crimes import *

#create player
gender = input("M or F\n")
firstName = Player.firstName(gender)
surnName = Player.surnName()
health = Player.health()
happiness = Player.happiness()
looks = Player.looks()
smarts = Player.smarts()
#parents
father = Player.createFather(surnName)
mother = Player.createMother(surnName)
birthDay = Player.birthday()
#RELATIONSHIPS
relationships = []
#BIRTH SCENARIO
scenario = "I was born " + Player.birthScenario() + " on " +birthDay
print("My name is " +firstName + " " + surnName)
print(scenario)
print("====== stats ======")
print("Health: " + str(health))
print("Looks; " + str(looks))
print("Smarts:" + str(smarts))
print("Happiness: " +str(happiness))
time.sleep(1)
deathChance = 0
#MAIN GAMEPLAY
print("PY LIFE 0.1\n")
alive = 1

age = 0
money = 0 #CHANGE THIS BACK TO 0 THIS IS A TEST VALUE
inPrison = False
agePrison = 0
sentence = 0
while alive == True:
    print("choose an option")
    print("1. activity")
    print("2. career")
    print("3. relationships (COMING SOON)")
    print("4. AGE UP")
    choice = input()
    if choice == "1":
        print("===== ACTIVITIES =====")
        print("1. doctor")
        print("2. have some 'happy' times")
        print("3. Go to school")
        print("4. Plastic surgery")
        print("5. Crimes")
        task = input()
        if task == "1":
            health = Activity.doctor(health)
            print("Health: " + str(health))
        if task == "2":
            happiness = Activity.happytimes(happiness)
            print("happiness: " +str(happiness))
        if task == "3":
            smarts = Activity.school(smarts)
            print("Smarts: " + str(smarts))
        if age >= 18:
            if task == "4":
                print("plastic surgery")
                potentialCost = [500, 1000,2000,5000,10000,15000,20000,5009,2013,4441,9076,12309]
                surgeryCost = r.choice(potentialCost)
                print("The surgery costs: £"+str(surgeryCost))
                print("Do you want to go ahead with this? Y or N")
                print("Currently have: £" + str(money))
                confirmation = input()
                if confirmation.upper() == "Y":
                    if money >= surgeryCost:
                        looks = Activity.plasticSurgery(looks)
                        money = money - surgeryCost
                        print("NEW LOOKS: "+ str(looks))
                        print("£"+str(money))
                    else:
                        print("YOu dont have enough")
                if confirmation.upper() == "N":
                    print("cancelled...")
            if task == "5":
                if inPrison == True:
                    print("you cannot commit crimes while in prison")
                
                else:
                    print("===== crimes =====")
                    print("1. robbery")
                    print("2. murder #mystery# - COMING SOON")
                    #etc
                    #etc
                    crime = input("Which one do you want to commit? ENTER NUMBER\n")
                    if crime == "1":
                        target = Robbery.target()
                        value = Robbery.value(target)
                        print("Target: "+target+ "Value: £"+str(value))
                        confirmation = input("do you want to?" "Y or N\n")
                        if confirmation.upper() == "Y":
                            success = Robbery.attempt(target)
                            if success == True:
                                money = money + value
                                print("£"+str(value)+" added to your bank account")
                            else:
                                #COMING SOON - DYNAMIC SENTENCE LENGTHS
                                inPrison = True
                                agePrison = age
                                sentence = 5
                                print("You were sentenced to y years in prison")
                
        if age <= 18 and task == "4":
            print("YOU ARE TOO YOUNG FOR THIS!!!")
        
    
    elif choice == "2":
        #list activities
        print("CAREER")
    
    elif choice == "3":
        #list relations
        print("RELATION")
    
    elif choice == "4":
        #DO AGE UP STUFF
        #random events
        print("AGEUP")
        health = Player.ageUp_health(health)
        looks = Player.ageUp_looks(looks)
        happiness = Player.ageUp_happiness(happiness)
        smarts = Player.ageUp_smarts(smarts)
        deathChance = Player.deathChance_inc(deathChance,age,happiness,health,smarts, inPrison)
        if (age - agePrison) == sentence:
            inPrison = False
        if inPrison == True:
            health = Player.prison_healthAgeUp(health)
            happiness = Player.prison_happinessAgeUP(happiness)
            looks = Player.prison_looksAgeUP(looks)
        print("====== stats ======")
        print("Health: " + str(health))
        print("Looks; " + str(looks))
        print("Smarts:" + str(smarts))
        print("Happiness: " + str(happiness))
        print("DeathChance: " + str(deathChance))
        print("InPrison: " +str(inPrison))
        print("\n")
        print("£"+str(money))
        age = age +1
        print("\n")
        print("AGE: " + str(age))
        alive = Player.deathRoller(deathChance, alive)
        print(alive)
    
print("RIP")

