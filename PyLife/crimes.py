import random as r
import time

class Crime:
    def depositMoney(money, gainsFromCrime):
        money = money+gainsFromCrime
        return money
    
    def robbery(inPrison, money):
        #each house will have its own success rate. 
        #the lower houses will be easier and the higher end houses will be harder to rob without
        #being arrested
        houses = ["mansion", "run down shed", "basic house"]

        target = r.choice(houses)

        if target == "basic house":
            potential_houseValue = [10962,21356,30342, 15000,17654,11769]
            houseValue = r.choice(potential_houseValue)
            print("you think about robbing a basic house with the value of: £" +houseValue)
            confirmation = input("ARE YOU SURE YOU WANT TO COMMIT THIS CRIME? Y or N")
            if confirmation.upper() == "Y":
                success = r.randint(1,100)
                if success >= 30:
                    print("successfully robbed...")
                    print("£"+str(houseValue)+" added to your account")
                    inPrison = False
                    return inPrison
            
                else:
                    print("you were arrested")
                    inPrison = True
                    return inPrison


            if confirmation.upper() == "N":
                print("you had some strange thoughts")

    
