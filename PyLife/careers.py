from email.mime import base
import random as r
import time

from numpy import take

class Apply:
    def jobTitle():
        potentialRoleTitle = ["police", "binman/lady", "game dev", "financial advisor", "actor of", "cleaner","diirector"]
        roleTitle = r.choice(potentialRoleTitle)
        return roleTitle#probably a better way tho lol
    
    def salary(roleTitle):
        #will revamp this to be more efficiant at somepoint
        if roleTitle =="police":
            salary = r.randint(50000,80000)

        elif roleTitle == "binman/lady":
            salary = r.randint(10000,20000)
        
        elif roleTitle == "game dev":
            salary = r.randint(60000,90000)
        
        elif roleTitle == "financial advisor":
            salary = r.randint(30000,60000)
        
        elif roleTitle == "actor of":
            salary = r.randint(100000,250000)
        
        elif roleTitle == "cleaner":
            salary = r.randint(30000,50000)
        
        elif roleTitle == "diirector":
            salary = r.randint(250000,500000)
        
        return salary

    def success(roleTitle, looks, happiness, smarts, health):
        
        # the baseline chance is as a percentage
        if roleTitle =="police":
            baselineChance = 30
            chance = baselineChance
            if health > 70:
                chance = chance + 10
            
            if smarts > 80:
                chance = chance + 20

        elif roleTitle == "binman/lady":
            baselineChance = 96
            chance = baselineChance
            if health > 50:
                chance = chance + 2
        
        elif roleTitle == "game dev":
            baselineChance = 50
            chance = baselineChance
            if smarts > 90:
                chance = chance + 20
        
        elif roleTitle == "financial advisor":
            baselineChance = 25
            chance = baselineChance
            if smarts > 78:
                chance = chance + 15
        
        elif roleTitle == "actor of":
            baselineChance = 25
            chance = baselineChance
            if looks > 90:
                chance = chance + 50
            
            if health > 80:
                chance = chance + 5
        
        elif roleTitle == "cleaner":
            baselineChance  = 85
            chance = baselineChance
            if health > 60:
                chance = chance + 2
        
        elif roleTitle == "diirector":
            baselineChance = 5
            chance = baselineChance
            if smarts > 78:
                chance = chance + 3
            
            if looks > 80:
                chance = chance + 5
            
        successRoll = r.randint(1,100)
        if successRoll <= chance:
            success = True
        
        else:
            success = False
        return success
        
class Quit:

    def jobRole(jobrole):
        jobrole = "none"
        return jobrole
    
    def salary(salary):
        salary = 0.00
        return salary

class Tax:
    
    def income(salary):
        if salary >20000 and salary < 50000:
            taxRate = 0.2
            toTaxSalary = salary - 12571
            taxedSalary = toTaxSalary * taxRate
            takeHomeSalary = salary - taxedSalary
        
        if salary > 50000 and salary < 150000:
            taxRate = 0.4
            toTaxSalary = salary - 12571
            taxedSalary = toTaxSalary * taxRate
            takeHomeSalary = salary - taxedSalary

        elif salary > 150000:
            taxRate = 0.43
            toTaxSalary = salary - 12571
            taxedSalary = toTaxSalary * taxRate
            takeHomeSalary = salary - taxedSalary

        else:
            takeHomeSalary = 0.00
        return takeHomeSalary