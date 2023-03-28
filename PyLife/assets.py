import random as r

#will be added soon
class Home:
    def type():
        homeTypes = ["Mansion", "apartment", "condo", "Salty Villa", "Cottage"]
        purchaseableHome = r.choice(homeTypes)
        return purchaseableHome
    def price(houseType):
        if houseType == "Mansion":
            potentialPrice = r.randint(1000000,100000000)
        elif houseType == "apartment":
            potentialPrice = r.randint(50000,200000)
        elif houseType == "condo":
            potentialPrice = r.randint(200000,450000)
        elif houseType == "Salty Villa":
            potentialPrice = r.randint(500000,100000000)
        elif houseType == "Cottage":
            potentialPrice = r.randint(250000,9000000)
        else:
            potentialPrice = r.randint(200000,500000)
        return potentialPrice
    def bills(houseType): #each year these will change either inc or dec
        #each housetype will have a different range
        if houseType == "Mansion":
            billValue = r.randint(300,500)
            yearlyBill = billValue * 12
        
        if houseType == "apartment":
            billValue = r.randint(50,200)
            yearlyBill = billValue * 12
        
        if houseType == "condo":
            billValue = r.randint(100,290)
            yearlyBill = billValue * 12
        
        if houseType == "Salty Villa":
            billValue = r.randint(400,500)
            yearlyBill = billValue * 12

        if houseType == "Cottage":
            billValue = r.randint(100,210)
            yearlyBill = billValue * 12
        
        else:
            billValue = r.randint(100,600)
            yearlyBill = billValue *12
        
        return yearlyBill
            
    #      ====== MORTGAGE =====
    def mortgage(money, potentialPrice):
        print("===== Mortgage Setup =====")
        deposit = input("Type in your deposit: £")
        return deposit
    
    def mortgageOutstanding(deposit, potentialPrice):
        outstanding = potentialPrice - int(deposit)
        return outstanding
    
    def mortgagePayment_Setup(money, outstanding):
        paymentValue = outstanding * 0.05 #5% a year
        paymentValue = float(paymentValue)
        return paymentValue
    
    def mortgagePayment(paymentValue, money):
        money = money - paymentValue
        return money

    def mortgagePayment_Outstanding(paymentValue, outstanding):
        outstanding = outstanding - paymentValue
        return outstanding

    #OUTRIGHT PAYMENT
    def purchaseOutright(money, potentialPrice):
        money = money - potentialPrice
        return money
    

class Car:
    def type():
        carTypes = ["Ferarri", "Lamborghini", "Ford", "Audi", "Nissan"]
        carType = r.choice(carTypes)
        return carType
    def model(carType):
        if carType == "Ferarri":
            modelNames = ["PuroSangue", "812 GTS", "296 GTB", "296 GTS", "F8 Trributo", "F8 Spider", "Roma"]
            model = r.choice(modelNames)
            return model
        elif carType == "Lamborghini":
            modelNames = ["Huracan", "Urus", "Adventador"]
            model = r.choice(modelNames)
            return model
        elif carType == "Ford":
            modelNames = ["Fiesta","Focus", "Escort", "Mondeo", "Taurus", "Mustang"]
            model = r.choice(modelNames)
            return model
        elif carType == "Audi":
            modelNames = ["A3","S3", "A4", "A5 Sportback", "A6", "A8", "Q3 e-tron"]
            model = r.choice(modelNames)
            return model
        elif carType == "Nissan":
            modelNames = ["Leaf","Juke", "X-trail", "Aria", "Qashqai"]
            model = r.choice(modelNames)
            return model
    def price(carType):
        if carType == "Ferarri":
            potentialPrice = r.randint(230000,600000)
        elif carType == "Lamborghini":
            potentialPrice = r.randint(200000,500000)
        elif carType == "Ford":
            potentialPrice = r.randint(20000,200000)
        elif carType == "Audi":
            potentialPrice = r.randint(19000,80000)
        elif carType == "Nissan":
            potentialPrice = r.randint(15000, 200000)
        else:
            potentialPrice = r.randint(10000,50000)
        return potentialPrice
    

    def loan(money):
        print("===== Car Loan Setup =====")
        deposit = input("Type in your deposit: £")
        return deposit
    
    def loanOutstanding(deposit, potentialPrice):
        outstanding = potentialPrice - int(deposit)
        return outstanding
    
    def loanPayment_Setup(money, outstanding):
        paymentValue = outstanding * 0.05 #5% a year
        paymentValue = float(paymentValue)
        return paymentValue
    
    def loanPayment(paymentValue, money):
        money = money - paymentValue
        return money

    def loanPayment_Outstanding(paymentValue, outstanding):
        outstanding = outstanding - paymentValue
        return outstanding