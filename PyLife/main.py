import random
import time
#import each quadrant of the game here
from player import Player
from activities import *
from crimes import *
from careers import *
from clearsave import *
from assets import *
from npc import *
from prison import *

#create player
print("===================================\n")
print("""______      _     _  __     
| ___ \    | |   (_)/ _|    
| |_/ /   _| |    _| |_ ___ 
|  __/ | | | |   | |  _/ _ \\
| |  | |_| | |___| | ||  __/
\_|   \__, \_____/_|_| \___|
       __/ |                
      |___/       \n""")
time.sleep(1)
print("Created by DoofusDragon | V0.2.5")
print("===================================\n")
time.sleep(3)
start = "null"
print("[1] New Life 👶")
print("[2] Clear Graveyard 💀")
while start != "1":
    start = input()
    if start == "2":
        clearGraveyard()
        print("graveyard cleared")
        print("[1] New Life 👶")
    elif start == "1":
        print("starting game")
print("Choose your character's gender")
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
print("My father is" + father)
print("My mother is "+mother)
print(scenario)
print("====== stats ======")
print("Health: " + str(health))
print("Looks; " + str(looks))
print("Smarts:" + str(smarts))
print("Happiness: " +str(happiness))
time.sleep(1)
deathChance = 0
#MAIN GAMEPLAY

alive = 1

age = 0
money = 0 #CHANGE THIS BACK TO 0 THIS IS A TEST VALUE
inPrison = False
agePrison = 0
sentence = 0
onMortgage = False

#CAREER STATS
roleTitle = ""
salary = 0.00
while alive == True:
    print("choose an option")
    print("1. activity")
    print("2. career")
    print("3. assets")
    print("4. AGE UP")
    choice = input()
    if choice == "1":
        print("===== ACTIVITIES =====")
        print("1. doctor")
        print("2. have some 'happy' times")
        print("3. Go to school")
        print("4. Plastic surgery")
        print("5. Crimes")
        print("6. Lottery")
        print("7. Gym")
        print("8. Party")
        if inPrison:
            print("I. Prison")
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
                    print("2. bank heist")
                    print("3. Hire a Hitman")
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
                                print("You were sentenced to "+str(sentence)+" years in prison")
                    
                    elif crime == "2":
                        potentialValue = BankHeist.value()
                        print("The banks portential value £"+str(potentialValue))
                        confirm = input("Do you want to do the heist(Y or N): ")
                        if confirm.lower() == "y":
                            crewCount = BankHeist.crewCount()
                            crewCut = BankHeist.crewCut(crewCount)
                            tools = BankHeist.tools(crewCount)
                            getawayVeichle_Type = BankHeist.getawayVeichle_Type(crewCount)
                            print("GetawayVeichleType: "+getawayVeichle_Type)
                            getawayVeichle_Speed = BankHeist.getawayVeichle_Speed(getawayVeichle_Type)
                            print("Veichle Speed: " +str(getawayVeichle_Speed)+ " MPH")
                            getawayVeichle_Cost = BankHeist.getawayVeichle_Cost(getawayVeichle_Type)
                            disguise_Type = BankHeist.disguise_Type(crewCount)
                            disguise_Cost = BankHeist.disguise_Cost(disguise_Type, crewCount)
                            totalSetupCost = BankHeist.totalSetupCost(tools, getawayVeichle_Cost, disguise_Cost)
                            print("TOTAL SETUP COST: £" +str(totalSetupCost))
                            confirmation = input("Are you willing to go ahead with this? Y or N: ")
                            if confirmation.lower() == "y":
                                if money < totalSetupCost:
                                    print("you cannot due to not having money")
                                    print("setup cost not deducted from account")
                                else:
                                    money = money - totalSetupCost
                                    print("You start the heist...")
                                    time.sleep(3)
                                    policeSpeed = BankHeist.policeSpeed()
                                    inPrison = BankHeist.arrested(policeSpeed, getawayVeichle_Speed, disguise_Type)
                                    if inPrison != True:
                                        potentialValue = float(potentialValue)
                                        crewCut = float(crewCut)
                                        money = BankHeist.depositMoney(potentialValue, crewCut)
                                    if inPrison != False:
                                        sentence = BankHeist.sentence(potentialValue)
                                        agePrison = age
                            
                            else:
                                print("you went back on your decision")
                        
                        else:
                            print("you went back on your choice.")

                    elif crime == "3":
                        target = HitmanHire.targetList()
                        price = HitmanHire.price()
                        reliability = HitmanHire.reliability()
                        success = HitmanHire.success(reliability)
                        print("The hitman charges you: £"+str(price))
                        confirm = input("Do you want to do this? Y OR N \n")
                        if confirm.lower() == "y":
                            inPrison = HitmanHire.scammer(success)
                        else:
                            print("you went back on your weird thoughts...")

        if age <= 18 and task == "4":
            print("YOU ARE TOO YOUNG FOR THIS!!!")
        
        if task == "6":
            if age < 16:
                print("you are too young")
            else:
                money = Activity.lottery(money)
        
        if task == "7":
            health = Activity.gym(health)
        
        if task == "8":
            happiness = Activity.party(happiness)
        
        if task.upper() == "I" and inPrison == True:
            print("===== PRISON =====")
            print("1. Escape")
            print("2. Riot")
            print("3. Pay to bail")
            select = input("Choose Number")
            if select == "1":
                inPrison = Escape.BlackJack() #will soon have several different ways that will be randomly selected
            
            elif select == "2":
                Riot.rally()
                inmateNPC_health = Riot.inmateNPC_Health()
                inmateNPC_smarts = Riot.inmateNPC_Smarts()
                guardNPC_health = Riot.guardNPC_Health()
                guardNPC_smarts = Riot.guardNPC_Smarts()
                inPrison = Riot.fight(inmateNPC_health, inmateNPC_smarts, guardNPC_health, guardNPC_smarts)
            
            elif select == "3":
                bailFee = Bail.fee(sentence)
                print(f"BAIL FEE: £{bailFee}")
                confirm = input("DO YOU WANT TO PAY THIS (Y OR N)\n")
                if confirm.upper() == "Y" and money >= bailFee:
                    print("YOU ARE FREE")
                    inPrison = False
                
                if confirm.upper() == "Y" and money <= bailFee:
                    print("you cannot afford this")

                if confirm.upper() == "N":
                    print("You did not pay the fee")
            else:
                print("INVALID")
                
        
    
    elif choice == "2":
        #CAREER
        print("CAREER")
        if age < 18:
            print("you are to young for this!")
        
        if inPrison:
            print("You cannot apply for a job whilst in prison!")

        else:
            print("1. APPLY")
            print("2. QUIT")
            task = input("Select using number ")
            if task == "1":
                if roleTitle == "":
                    roleTitle_Apply = Apply.jobTitle()
                    salary_Apply = Apply.salary(roleTitle_Apply)
                    print("JOB OPENING")
                    print(roleTitle_Apply + "paying £"+str(salary_Apply))
                    confirm = input("Do you want to apply? Y or N ")
                    if confirm.lower() == "y":
                        successful = Apply.success(roleTitle_Apply, looks, happiness, smarts, health)
                        if successful:
                            roleTitle = roleTitle_Apply
                            salary = salary_Apply
                            print("CONGRATS: you got the job")
                        else:
                            print("you did not get the job")
            
                    if confirm.lower() == "n":
                        print("you did not apply in the end.")
                else:
                    print("please quit your current job first")
            
            elif task == "2":
                if roleTitle != "":
                    roleTitle = Quit.jobRole(roleTitle)
                    salary = Quit.salary(salary)
                else:
                    print("You cant quit as you have no job")
    
    elif choice == "3":
        print("===== ASSETS =====")
        print("1. Purchase Home")
        print("2. Purchase Car (SOON)")
        print("3. Sell Home (SOON)")
        print("4. Sell Car (SOON)")
        select = input("Select using a corresponding number")
        if select == "1":
            houseType = Home.type()
            housePrice = Home.price(houseType)
            print("===HOUSE FOR SALE===")
            print(houseType +"for £"+str(housePrice)+"\n")
            print("=== PURCHASE OPTIONS ===")
            print("M. Mortgage")
            print("P. Purchase with cash")
            print("C. Cancel purchase")
            select = input("select an option\n")
            if select.lower() == "m":
                deposit = Home.mortgage(money, housePrice)
                toPay = Home.mortgageOutstanding(deposit, housePrice)
                paymentValue = Home.mortgagePayment_Setup(money, toPay)
                money = Home.mortgagePayment(paymentValue, money)
                print("Mortgage taken success!")
                onMortgage = True
            
            elif select.lower() == "p":
                if money >= housePrice:
                    money = Home.purchaseOutright(money, housePrice)
                else:
                    print("You cannot purchase")
                    print("PURCHASE CANCELLED BY DEFAULT...")

    
    elif choice == "4":
        #DO AGE UP STUFF
        #random events
        print("AGEUP\n")
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
            roleTitle = Quit.jobRole(roleTitle)
            salary = Quit.salary(salary)
        
        if onMortgage == True:
            toPay = Home.mortgagePayment_Outstanding(paymentValue, toPay)
            #paymentValue = Home.mortgagePayment_Setup(money, toPay)
            money = Home.mortgagePayment(paymentValue, money)
            toPay = round(toPay,2)
            print(f"£{toPay}left on mortgage")
            if toPay <= 0:
                onMortgage = False

        
        money = money + Tax.income(salary)
        money = round(money, 2)
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
        #print(alive)
    
print("RIP")
print("===== Grave =====")
print("Name: " +firstName + " "+ surnName)
print("Lived Until: "+str(age)+" years")
if inPrison:
    print("They died in custody")
if happiness > 80:
    print("They were a happy person")

if happiness < 10:
    print("they werent too happy")

if health > 80:
    print("they were very healthy")

f = open("graveyard.txt", "a")
f.write("===== Grave =====")
f.write("\n")
f.write("Name: " +firstName + " "+ surnName)
f.write("\n")
f.write("Lived Until: "+str(age)+" years")
f.write("\n")
if inPrison:
    f.write("They died in custody")
    f.write("\n")
if happiness > 80:
    f.write("They were a happy person")
    f.write("\n")

if happiness < 10:
    f.write("they werent too happy")
    f.write("\n")

if health > 80:
    f.write("they were very healthy")
    f.write("\n")

f.write("================================")
f.write("\n")
f.close()