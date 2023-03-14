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