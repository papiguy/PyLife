from npc import *
import random as r
class Friend:
    def gender():
        roll = r.randint(1,2)
        if roll == 2:
            gender = "M"
        
        else:
            gender = "F"

        return gender
    
    def age(playerAge):
        older = r.randint(1,2)
        if older == 1:
            age = playerAge + r.randint(0,2)
        else:
            age = playerAge - r.randint(0,2)
            if age < 0:
                age = 0
        
        return age
    
    def name(gender):
        if gender.lower() == "f":
            firstNames_F = ["Sophie","Jess","Priscilla","Amy", "Chloe","Layla", "Laura", "Sharron", "Hannah","Emily"]
            firstName = r.choice(firstNames_F)
        elif gender.lower() == "m":
            firstNames_M = ["John", "Hubert", "Joe", "Dave", "Lachlan", "Bill", "Ryan","Josh", "Sam", "Joeseph", "Grant", "Eean"]
            firstName = r.choice(firstNames_M)
        
        else:
            print("Something went wrong...")
            firstName = "name"
        
        surnNames = ["Boadi", "Omoregie", "Wisneieski", "Johnson", "Dumb", "McDonald", "Power","Alken", "Middleton", "Small", "Big", "Loiken"]
        surnName = r.choice(surnNames)

        fullName = firstName + " " + surnName
        return fullName
    #comes after naming
    def makeStats(): #stats dont really matter apart from initially
        looks = NPC.looks()
        happiness = NPC.happiness()
        smarts = NPC.smarts()
        health = NPC.health()
        craziness = NPC.craziness()
        money = NPC.money()
        print("===== Friend Stats =====")
        print(f"Health: {health}")
        print(f"Happiness: {happiness}")
        print(f"Looks: {looks}")
        print(f"Smarts: {smarts}")
        print(f"Craziness: {craziness}")
        print(f"Money: {money}")

    def meetPlayer(playerLooks, playerSmarts):
        roll = r.randint(1,100)
        if playerLooks > 60:
            roll = roll +5
        elif playerLooks < 20:
            roll = roll - 5
        if playerSmarts > 60:
            roll = roll + 5
        elif playerSmarts < 20:
            roll = roll - 3

        if roll > 50:
            return True
        else:
            return False
        
    def initialLikeness(playerHappiness, playerLooks, playerSmarts):
        defaultLikeness = 50
        likeness = defaultLikeness

        if playerHappiness > 70:
            likeness = likeness + 3
        elif playerHappiness < 20:
            likeness = likeness - 5
        
        if playerLooks > 70:
            likeness = likeness + 3
        elif playerLooks < 20:
            likeness = likeness - 3
        
        if playerSmarts > 70:
            likeness = likeness + 3
        elif playerSmarts < 20:
            likeness = likeness - 3
        
        return likeness
    

class Friend_Romantic:
    def gender():
        roll = r.randint(1,2)
        if roll == 2:
            gender = "M"
        
        else:
            gender = "F"

        return gender
    
    def age(playerAge):
        older = r.randint(1,2)
        if older == 1:
            age = playerAge + r.randint(0,2)
        else:
            age = playerAge - r.randint(0,2)
            if age < 0:
                age = 0
        
        return age
    
    def name(gender):
        if gender.lower() == "f":
            firstNames_F = ["Sophie","Jess","Priscilla","Amy", "Chloe","Layla", "Laura", "Sharron", "Hannah","Emily"]
            firstName = r.choice(firstNames_F)
        elif gender.lower() == "m":
            firstNames_M = ["John", "Hubert", "Joe", "Dave", "Lachlan", "Bill", "Ryan","Josh", "Sam", "Joeseph", "Grant", "Eean"]
            firstName = r.choice(firstNames_M)
        
        else:
            print("Something went wrong...")
            firstName = "name"
        
        surnNames = ["Boadi", "Omoregie", "Wisneieski", "Johnson", "Dumb", "McDonald", "Power","Alken", "Middleton", "Small", "Big", "Loiken"]
        surnName = r.choice(surnNames)

        fullName = firstName + " " + surnName
        return fullName
    #comes after naming
    def makeStats(): #stats dont really matter apart from initially
        looks = NPC.looks()
        happiness = NPC.happiness()
        smarts = NPC.smarts()
        health = NPC.health()
        craziness = NPC.craziness()
        money = NPC.money()
        print("===== Friend Stats =====")
        print(f"Health: {health}")
        print(f"Happiness: {happiness}")
        print(f"Looks: {looks}")
        print(f"Smarts: {smarts}")
        print(f"Craziness: {craziness}")
        print(f"Money: {money}")

    def meetPlayer(playerLooks, playerSmarts):
        roll = r.randint(1,100)
        if playerLooks > 60:
            roll = roll +5
        elif playerLooks < 20:
            roll = roll - 5
        if playerSmarts > 60:
            roll = roll + 5
        elif playerSmarts < 20:
            roll = roll - 3

        if roll > 50:
            return True
        else:
            return False
        
    def initialLikeness(playerHappiness, playerLooks, playerSmarts):
        defaultLikeness = 50
        likeness = defaultLikeness

        if playerHappiness > 70:
            likeness = likeness + 3
        elif playerHappiness < 20:
            likeness = likeness - 5
        
        if playerLooks > 70:
            likeness = likeness + 3
        elif playerLooks < 20:
            likeness = likeness - 3
        
        if playerSmarts > 70:
            likeness = likeness + 3
        elif playerSmarts < 20:
            likeness = likeness - 3

        return likeness
# add more Romantic_Friend stuff later

class FriendActivity:
    def spendTimeWith(relationships_Friend, relationships_Romantic, likeness_Friend, likeness_Romantic):
        friendValid = True
        R_friendValid = True
        spendTime_activities = ["went on a walk", "went to tesco"]
        if len(relationships_Friend) < 1:
            print("You got no friends")
            return False
        else:
            print(relationships_Friend)
            choose = input("Please select a friend (use number)")
            choose = int(choose)
            friend = relationships_Friend[choose -1]
            friendLikeness = likeness_Friend[choose -1]
            spendTime_activity = r.choice(spendTime_activities)
            print(f"you {spendTime_activity} with {friend}")
            selected = choose -1
            return selected
    
    def askOut(relationships_Friend, friendLikeness):
        if len(relationships_Friend) < 1:
            print("No one to ask")
            return False
        
        else:
            print(relationships_Friend)
            choose = input("Please select a friend (use number)\n")
            choose = int(choose)
            friend = relationships_Friend[choose -1]
            likeness = friendLikeness[choose - 1]
            confirmation = input("Confirm? Y or N\n")
            if confirmation.lower() == "y":
                successRoll = r.randint(1,100)
                if likeness > 70:
                    successRoll = successRoll + 3
                if successRoll <= 100:
                    pos = choose -1
                    return pos
                else:
                    return False
    
    def compliment(friend_Relationships, friendLikeness):
        print(friend_Relationships)
        choose = input("pick a friend (use number)")
        choose = int(choose)
        friend = friend_Relationships[choose - 1]
        print(f"you compliment {friend}")
        appreciation = r.randint(1,100)
        print(f"their appreciation: {appreciation}/100")
        pos = choose-1
        return pos
    
class FriendActivity_R:
    def spendTimeWith(relationships_Romantic, likeness_Romantic):
        friendValid = True
        R_friendValid = True
        spendTime_activities = ["went on a walk", "went to tesco"]
        if len(relationships_Romantic) < 1:
            print("You got no friends")
            return False
        else:
            print(relationships_Romantic)
            choose = input("Please select a friend (use number)")
            choose = int(choose)
            friend = relationships_Romantic[choose -1]
            friendLikeness = likeness_Romantic[choose -1]
            spendTime_activity = r.choice(spendTime_activities)
            print(f"you {spendTime_activity} with {friend}")
            selected = choose -1
            return selected
    
    def compliment(friend_Relationships, friendLikeness):
        print(friend_Relationships)
        choose = input("pick a friend (use number)")
        choose = int(choose)
        friend = friend_Relationships[choose - 1]
        print(f"you compliment {friend}")
        appreciation = r.randint(1,100)
        print(f"their appreciation: {appreciation}/100")
        pos = choose-1
        return pos

class Child:
    def gender():
        gender = NPC.gender()
        return gender
    
    def name(gender ,surnName):
        boyNames = ["Shaun", "Joe", "Ryan", "Euan", "Eduardo", "Burt", "Graham", "Grant"]
        girlNames = ["Layla", "Sophie", "Elizabeth", "Emily", "Charlotte"]
        name = input("What do you want to name your child or type R for random name!\n")
        if name.upper() == "R":
            if gender.upper() == "M":
                name = r.choice(boyNames)
            elif gender.upper() == "F":
                name = r.choice(girlNames)
            
        fullName = name + " " + surnName
        
        return fullName

    def birthSuccess(playerHappiness, PlayerHealth):
        success = r.randint(1,100)
        if playerHappiness > 70:
            success = success + 3
        elif playerHappiness < 25:
            success = success - 1
        if PlayerHealth > 70:
            success = success + 3
        elif PlayerHealth < 25:
            success = success - 2
        
        if success > 40:
            return True
        else:
            return False

    def makeStats(playerHealth, playerSmarts, playerLooks, playerHappiness, childName):
        health = NPC.health()
        happiness = NPC.happiness()
        looks = NPC.looks()
        smarts = NPC.smarts()
        if playerHealth > 70:
            health = health + r.randint(1,3)
            if health > 100:
                health = 100
        
        elif playerHealth < 25:
            health = health - r.randint(1,3)
            if health < 5:
                health = 5

        if playerSmarts > 70:
            smarts = smarts + r.randint(1,3)
            if smarts > 100:
                smarts = 100
        
        elif playerSmarts < 25:
            smarts = smarts - r.randint(1,3)
            if smarts < 0:
                smarts = 0
        
        if playerHappiness > 70:
            happiness = happiness + r.randint(1,3)
            if happiness > 100:
                happiness = 100
            
        elif playerHappiness < 25:
            happiness = happiness - r.randint(1,3)
            if happiness < 0:
                happiness = 5

        if playerLooks > 70:
            looks = looks + r.randint(1,3)
            if looks > 100:
                looks = 100
        
        elif playerLooks < 25:
            looks = looks - r.randint(1,3)
            if looks < 0:
                looks = 0
        
        print(f"===== {childName}'s stats =====")
        print(f"Health: {health}")
        print(f"Happiness: {happiness}")
        print(f"Smarts: {smarts}")
        print(f"Looks: {looks}")
    
    def cost(children_array):
        totalCost = 0.00
        for i in range(0, len(children_array)+1):
            costPerYear = r.randint(500, 2000)
            totalCost = totalCost + costPerYear

        return totalCost
    
    def spendTimeWith(children_array):
        spendTimeTasks = ["on a walk","to the park", "to the supermarket"]
        activity = r.choice(spendTimeTasks)
        enjoyment = r.randint(1,100)
        print(children_array)
        select = 0

        try:
            select = int(input("use number to select child"))
        
        except TypeError:
            print("Invalid Input!")
            print("Picking random child")
        
        except ValueError:
            print("Invalid Input")
            print("Picking random child")


        child = children_array[select -1]
        print(f"you take {child} {activity}")
        print(f"Their enjoyment {enjoyment}/100")