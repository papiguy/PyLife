import random as r

class Player:

    #players stats
    def health():
        health = r.randint(1,100)
        return health
    
    def looks():
        looks = r.randint(1,100)
        return looks
    
    def happiness():
        happiness = r.randint(1,100)
        return happiness
    
    def smarts():
        smarts = r.randint(1,100)
        return smarts
    
    #players Name
    def firstName(gender):
        if gender.upper() == "M":
            maleNames = ["John", "Hubert", "Joe", "Dave", "Lachlan", "Bill"]
            name = r.choice(maleNames)

        if gender.upper() == "F":
            femaleNames = ["Sophie","Jess","Priscilla","Amy", "Chloe"]
            name= r.choice(femaleNames)
            
        return name
    
    def surnName():
        surnNames = ["Boadi", "Omoregie", "Wisneieski", "Johnson", "Dumb", "McDonald", "Power"]
        lastName = r.choice(surnNames)
        return lastName
    #players Family
    def createMother(surnName):
        motherNames = ["Sophie","Jess","Priscilla","Amy", "Chloe"]
        firstName = r.choice(motherNames)
        mumName = firstName + surnName
        return mumName
    
    def createFather(surnName):
        fatherNames = ["Sophie","Jess","Priscilla","Amy", "Chloe"]
        firstName = r.choice(fatherNames)
        dadName = firstName + surnName
        return dadName
    
    def birthday():
        months = ["January","February", "March", "April", "May", "June", "July", "August","September","October", "November", "December"]
        birthMonth = r.choice(months)
        birthDate = r.randint(1,28)

        birthDay = birthMonth +" "+  str(birthDate)
        return birthDay
    
    def birthScenario():
        scenarios = ["in a hospital", "in a car", "in a school", "next to joe biden", "in tax"]

        born = r.choice(scenarios)
        return born
    
    def deathRoller(deathChance, alive):
        roll = r.randint(1,100)
        if roll < deathChance:
            alive = False
        else:
            alive = True
        return alive

    def deathChance_inc(deathChance, age, happiness, health, smarts, inPrison):
        if age < 60:
            deathChance = deathChance + 0

        if age > 60:
            deathChance = deathChance + 0.5
        
        if age > 70:
            deathChance = deathChance + 1
        
        if age > 85:
            deathChance = deathChance + 1.5
        
        if age > 90:
            deathChance = deathChance + 5
        
        if happiness > 80:
            deathChance = deathChance - 1
        
        if happiness < 25 and happiness > 10:
            deathChance = deathChance + 0.3
        
        if happiness < 10:
            deathChance = deathChance + 4.5

        if health > 80:
            deathChance = deathChance - 3
        
        if health < 25 and health > 10:
            deathChance = deathChance + 1

        if smarts < 10:
            deathChance = deathChance + 0.1
        
        if inPrison == True:
            deathChance = deathChance + 0.3

        if deathChance < 0:
            deathChance = 0

        return deathChance
    
    #AGEUP STATS

    def ageUp_health(health):
        increase = r.randint(1,10)
        if increase >= 5:
            act_Increase = r.randint(1,5)
            health = health + act_Increase
        
        if increase <5:
            act_Decrease = r.randint(1,5)
            health = health - act_Decrease

        if health > 100: 
            health = 100
        
        if health < 0:
            health = 0
        
        return health
    
    def ageUp_looks(looks):
        increase = r.randint(1,10)
        if increase >= 5:
            act_Increase = r.randint(1,5)
            looks = looks + act_Increase
        
        if increase <5:
            act_Decrease = r.randint(1,5)
            looks = looks - act_Decrease

        if looks > 100:
            looks = 100
        
        if looks < 0:
            looks = 0
        
        return looks
    
    def ageUp_happiness(happiness):
        increase = r.randint(1,10)
        if increase >= 5:
            act_Increase = r.randint(1,5)
            happiness = happiness + act_Increase
        
        if increase <5:
            act_Decrease = r.randint(1,5)
            happiness = happiness - act_Decrease
        
        if happiness > 100:
            happiness = 100
        
        if happiness < 0:
            happiness = 0
        
        return happiness
    
    def ageUp_smarts(smarts):
        increase = r.randint(1,10)
        if increase >= 5:
            act_Increase = r.randint(1,5)
            smarts = smarts + act_Increase
        
        if increase <5:
            act_Decrease = r.randint(1,5)
            smarts = smarts - act_Decrease

        if smarts > 100:
            smarts = 100
        
        if smarts < 0:
            smarts = 0
        
        return smarts
    

    #these are now all RANDOM EVENTS THAT COULD AFFECT THE PLAYER AND REQUIRE ACTION
    #COMING SOON        