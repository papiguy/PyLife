import random as r
import time

class NPC:

    def smarts():
        smarts = r.randint(1,100)
        return smarts

    def looks():
        looks = r.randint(1,100)
        return looks

    def happiness():
        happiness = r.randint(1,100)
        return happiness

    def health():
        health = r.randint(1,100)
        return health

    def craziness():
        craziness = r.randint(1,100)
        return craziness

    def money():
        money = r.randint(1,100)
        return money
        
    def generosity():
        generosity = r.randint(1,100)
        return generosity

    def gender():
        selector = r.randint(1,2)
        if selector == 1:
            gender = "M"
        elif selector == 2:
            gender = "F"
        return gender
    def firstname(gender):
        maleNames = ["Joe", "Shaun", "Jeremiah", "Jordan", "Harry",
        "Jeff", "Hubert", "Ed", "Jebediah", "Bob", "Ryan", "Dylan",
        "Theo", "Wilson", "Dan", "Allan", "Jack", "Alexander","Syed"]

        femaleNames = ["Sophia", "Priscilla", "Layla", "Ella", "Ellen",
        "Alex", "Jess", "Jodie", "Jemma", "Sophie", "Elenor", "Louise"]

        if gender == "M":
            firstName = r.choice(maleNames)
        elif gender == "F":
            firstName = r.choice(femaleNames)
        return firstName
    def lastname():
        lastNames = ["Boadi", "Wisneiwski", "Budzynski", "Murad", "Parry", "Johnson",
        "Poorst", "Hearst", "Coldest", "Boldest", "Bridest", "Pether-Ridgerd"]
        lastName = r.choice(lastNames)
        return lastName
    def age(PlayerAge):
        if PlayerAge < 17 and PlayerAge > 10:
            age = r.randint(11,16)
        else:
            age = r.randint(20,80)
        
        return age

    def occupation():
        roleTitles = ["Nurse", "police officer", "College Lecturer", "Tax Person",
        "Relationship Counsellor", "Movie Star", "YouTuber", "BodyGuard", 
        "Personal Trainer", "Game Developer", "Game Tester", "PyLife Developer"]
        jobRole = r.choice(roleTitles)
        return jobRole
