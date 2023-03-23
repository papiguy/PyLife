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
