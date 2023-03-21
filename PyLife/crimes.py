import random as r
import time

class Robbery:
    def target():
        targets = ["basic house", "shed", "mansion", "keyboard villa"]
        target = r.choice(targets)
        return target
    
    def value(target):
        if target == "basic house":
            potentialValues = [12412,23689,25971,5230]
            value = r.choice(potentialValues)
        
        elif target == "shed":
            potentialValues = [122,420,539,823,1032]
            value = r.choice(potentialValues)
        
        elif target == "mansion":
            potentialValues = [502345,75873,90357,100780,123090,109999]
            value = r.choice(potentialValues)

        elif target == "keyboard villa":
            potentialValues = [100000,250000,507777,1079902]
            value = r.choice(potentialValues)
        
        return value
        
    def attempt(target):
        if target == "basic house":
            failChance = 20
        elif target == "shed":
            failChance = 2
        elif target == "mansion":
            failChance = 65
        elif target == "keyboard villa":
            failChance = 85

        successRoll = r.randint(1,100)
        if successRoll > failChance:
            return True
        else:
            return False
        
class BankHeist:
    def value():
        value = r.randint(1000000,200000000)
        return value
    
    #SETUP THE HEIST
    def crewCount():
        valid = False
        while valid == False:
            crewCount = int(input("How many people would you like on this heist? Enter a number (Max 5) "))
            if crewCount > 5:
                print("too many!")
            else:
                valid = True
                return crewCount
    def crewCut(crewCount):
        if crewCount > 0:
            cut = input("How much of the final cut should each crew memebr recieve (%) ")
            cut = float(cut)
            cut = cut / 100
            cut = float(cut)
        else:
            cut = 0.0
        return cut

        
    def tools(crewCount):
        if crewCount == 0:
            crewCount = crewCount +1
        toolCost = r.randint(1000,25000)
        totalToolCost = toolCost * crewCount

        return totalToolCost
    #any "getawayVeichle_[attribute] defines the veichles stats and type"
    def getawayVeichle_Type(crewCount):
        if crewCount == 0:
            crewCount = crewCount+1
        
        if crewCount <= 2:
            getawayVeichle_Type = "motorcycle"

        if crewCount > 2 and crewCount < 5:
            getawayVeichle_Type = "sedan"
        
        if crewCount >= 5:
            getawayVeichle_Type = "van"
        
        return getawayVeichle_Type
    
    def getawayVeichle_Cost(getawayVeichle_Type):
        if getawayVeichle_Type == "motorcycle":
            lowerCost = 2500
            upperCost = 7000
        if getawayVeichle_Type == "sedan":
            lowerCost = 5000
            upperCost = 15000
        if getawayVeichle_Type == "van":
            lowerCost = 10000
            upperCost = 20000
        
        cost = r.randint(lowerCost,upperCost)
        return cost
    
    def getawayVeichle_Speed(getawayVeichle_Type):
        if getawayVeichle_Type == "motorcycle":
            maxSpeed = 300
            minSpeed = 80
        if getawayVeichle_Type == "sedan":
            maxSpeed = 200
            minSpeed = 80
        if getawayVeichle_Type == "van":
            maxSpeed = 150
            minSpeed = 80
        
        speed = r.randint(minSpeed,maxSpeed)
        return speed
    #defines the attributes of disguise_[attribute]
    def disguise_Type(crewCount):
        disguises = ["security", "bug exterminators", "basic masks", "none"]
        print("1. security = HIGH POTENTIAL COST")
        print("2. bug exterminators = MEDIUM POTENTIAL COST")
        print("3. Basic masks = LOW POTENTIAL COST")
        print("4. None - NO COST")
        type = int(input("Choose a disguise using the accociated number: "))
        if type == 1:
            disguiseUsed = disguises[0]
        if type == 2:
            disguiseUsed = disguises[1]
        if type == 3:
            disguiseUsed = disguises[2]
        if type == 4:
            disguiseUsed = disguises[3]
        return disguiseUsed
    
    def disguise_Cost(disguise_Type, crewCount):

        maxCost = 1
        minCost = 0
        if disguise_Type == "security":
            minCost = 2500
            maxCost = 25000
        if disguise_Type == "bug exterminators":
            minCost = 1000
            maxCost = 10000
        if disguise_Type == "basic masks":
            minCost = 500
            maxCost = 2500
        
        cost = r.randint(minCost,maxCost)
        if disguise_Type =="none":
            cost = 0
        
        totalCost = cost * crewCount
        
        return totalCost
    #def hacking
    def totalSetupCost(tools, getawayVeichle, disguise): #,hacking may be readded soon
        total = int(tools) + int(getawayVeichle) + int(disguise) #+ hacking
        return total
    
    #GETAWAY SYSTEM

    #POLICE
    def policeSpeed():
        minSpeed = 78
        maxSpeed = 299
        speed = r.randint(minSpeed, maxSpeed)
        return speed
    
    def arrested(policeSpeed, getawayVeichle_Speed, disguise):
        if disguise == "security":
            policeSpeed = policeSpeed - 15
        if disguise == "bug exterminators":
            policeSpeed = policeSpeed - 5
        if disguise == "basic masks":
            policeSpeed = policeSpeed - 2
        if disguise == "none":
            policeSpeed = policeSpeed - 0
        
        if policeSpeed > getawayVeichle_Speed:
            return True
        else:
            return False

    def sentence(value):
        sentence = 0
        for i in range(1,value, 900000):
            sentence = sentence + 1
        
        print("You were arrested and sent to prison for: " +str(sentence)+"years")
        
        return sentence
    
    def depositMoney(value, crewCut):
        finalCrewCut = crewCut * value
        playerTake = value - finalCrewCut
        print("===== HEIST RESULTS =====")
        print("TOTAL TAKE: £"+str(value))
        print("CREW CUT: "+str(crewCut*100)+"%")
        print("YOUR TAKE: £"+str(playerTake))
        return playerTake

class HitmanHire:
    def targetList():
        namedTargets = ["Boris","Vinny", "Bob","satine", "John"]
        roledTargets = ["Youtuber","police","GameDev", "Web Dev", "Random Nerd"]
        potentialTarget1 = r.choice(namedTargets)
        potentialTarget2 = r.choice(roledTargets)

        print("You are thinking of hiring a hitman to take out: "+potentialTarget1 + " OR a "+ potentialTarget2)
        selectedTarget = input("Who will you take care of? 1 OR 2\n")
        if selectedTarget == "1":
            return potentialTarget1
        else:
            return potentialTarget2
        
    def price():
        price = r.randint(100000,500000)
        return price
    
    def reliability():
        reliability = r.randint(1,100) # basically this will help with success roles, if lower than value = success
        return reliability
    
    def success(reliability):
        successRoll = r.randint(1,100)
        if successRoll <= reliability:
            success = True
        else:
            success = False
        return success

    def scammer(success):
        if success:
            inPrison = False

            print("The hitman carried out the work")
        else:
            chance = r.randint(1,5)
            if chance == 1:
                inPrison = True
                print("The hitman reported you to the authorities")
            else:
                inPrison = False
            
        return inPrison
