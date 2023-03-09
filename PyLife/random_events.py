import random as r
import time

class RandomEvent:
    def AgeUpEvent():
        possibleEvents = ["Your mother ate squidward"]
        chance = r.randint(1,100)
        if chance <= 25:
