import random as r
import time


class Activity:
    def doctor(health):
        #roll random illness for the funny
        #if they are not ill they gain health
        #if they are ill they lose hp
        ill = r.randint(1,100)
        if ill > 50:
            print("YOU ARE ILL")
            #now FOR THE FUNNY IT WILL ROLL WHETHER THEY GAIN HEALTH OR LOSE SOME HAHA
            healed = r.randint(1,100)
            if healed > 50: 
                print("You are healed")
                health = health + r.randint(1,10)
                if health > 100:
                    health = 100
            
            if healed <= 50:
                print("You are healed but it damaged you in the process")
                health = health - r.randint(1,9)

        if ill <= 50:
            print("You are not ill")
            health = health + 3
        
        return health
    
    def school(smarts):
        lessons = ["drama", "computer science", "business", "PSHE", "Tax Lesson"]
       
        print("You attend a lesson")
        classSelected = r.choice(lessons)
        if classSelected == "Tax Lesson":
            print("you learnt absolutely nothing in the three hours")
            smarts = smarts - 25
            if smarts < 0:
                smarts = 0
        else:
            increase = r.randint(1,100)
            if increase > 50:
                print("you learn something")
                amount = r.randint(1,10)
                smarts = smarts + amount
                if smarts > 100:
                    smarts = 100
            if increase <= 50:
                print("you got confused")
                amount = r.randint(1,10)
                smarts = smarts - amount
                if smarts < 0:
                    smarts = 0
        return smarts
    
    def happytimes(happiness):
        happyActivity = ["spent time with family", "went on a wok", "you cranked 90s on fortnite"]
        activity = r.choice(happyActivity)
        enjoymentScale = r.randint(1,100)
        print("you " + activity)
        print("you enjoyed it: " +str(enjoymentScale)+"/100")
        if enjoymentScale < 25 and enjoymentScale > 10:
            happiness = happiness - r.randint(1,3)
        if enjoymentScale < 10:
            happiness = happiness - r.randint(3,10)
        if enjoymentScale > 25 and enjoymentScale < 75:
            happiness = happiness + r.randint(1,5)
        if enjoymentScale > 75 and enjoymentScale < 90:
            happiness = happiness + r.randint(3,10)
        else:
            happiness = happiness + r.randint(5,15)
        
        if happiness > 100:
            happiness = 100
        if happiness < 0:
            happiness = 0
        
        return happiness
    
    def plasticSurgery(looks):
        print("undertaking surgery...")
        success = r.randint(1,100)
        if success > 50:
            print("SURGERY WAS SUCCESSFUL - LOOKS IMPROVED")
            looks = looks + r.randint(1, 10)
            if looks > 100:
                looks = 100
        if success <= 50:
            print("SURGERY FAILED - LOOKS MESSED UP")
            looks = looks - r.randint(1,10)

        return looks


    def lottery(money):
        costToEnter = r.randint(1,25)
        jackpot = r.randint(100000,900000000)
        print("To enter the lottery it costs: £"+str(costToEnter))
        print("PRIZE: £" +str(jackpot))
        confirm = input("Y or N\n")
        if confirm.lower() == "y":
            chance = r.randint(1,100)
            if chance == 1:
                print("YOU WON THE LOTTERY!")
                money = money + jackpot
                return money
            
            else:
                money = money - costToEnter
                return money
            
    def gym(health):
        print("you go to the gym and its beneficial")
        gains = r.randint(1,25)#
        health = health + gains
        if health > 100:
            health = 100
        return health
    

    def party(happiness):
        happyActivity = ["went to a pub", "went to a night club", "went to a bar", "went to a friends home"]
        activity = r.choice(happyActivity)
        enjoymentScale = r.randint(1,100)
        print("you " + activity)
        print("you enjoyed it: " +str(enjoymentScale)+"/100")
        if enjoymentScale < 25 and enjoymentScale > 10:
            happiness = happiness - r.randint(1,3)
        if enjoymentScale < 10:
            happiness = happiness - r.randint(1,3)
        if enjoymentScale > 25 and enjoymentScale < 75:
            happiness = happiness + r.randint(1,5)
        if enjoymentScale > 75 and enjoymentScale < 90:
            happiness = happiness + r.randint(3,10)
        else:
            happiness = happiness + r.randint(5,15)
        
        if happiness > 100:
            happiness = 100
        if happiness < 0:
            happiness = 0
        
        return happiness