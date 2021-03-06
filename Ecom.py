# %%
# Comment above activates interactive mode while using Pylance, nessasary to plot graphs. Jupyter Notebook works to, of course.a
import matplotlib.pyplot as plt
import statistics as stats
from random import randint as ri
from random import shuffle as shuf
# Note that I explain the variables in the order in wich they are in enabled. To genuinly implement classes, do it in order of __init__ apearence.
# self is not a variable but a self-reference tools that allow you to identify variables via modules of something in that class. Thus all the "self dot"s.
class Product: # This is what is being sold in the market. 
    def __init__(self, fet1, fet2, fet3): #It takes three numbers, represeting different fetures of the prduct.
        self.fet1 = fet1
        self.fet3 = fet3
        self.fet2 = fet2
        self.price9 = fet1 * 2 + fet2 * 3 + fet3 * 6 # What it cost to by the parts from the monopolies that sell them: as a function of the fetures. 
class Seller: # The store.
    def __init__(self, name, price, quan, prod, money, cap, vis, min, income, transactions):
        self.trans = transactions # a list of payments to the store. 
        self.inc =  income # The monthly earnings of the store.
        self.id = name
        self.min = min # The mininum price the store is willing to sell.
        self.vis = vis # A Boolean asking if a trasaction has been made today. Always starts out False. 
        self.cap = cap # How many product fit in the store.
        self.price = price # The current pricing of their Product. 
        self.quan = quan # How many products they have.
        self.prod = prod #  A Class Product(see above). Sellers are the providers.
        self.mon = money # How much money I have.
class Buyer: # The Buyer
    def __init__(self, name, wfet1, wfet2, wfet3, Buget, max, minwfet1, minwfet2, minwfet3):
        self.max = max # The maximum price they are willing to buy at. 
        # Next three variables are the miminum requirements for each feture if they are going to buy it.
        self.id = name
        self.wfet1 = wfet1 
        self.wfet2 = wfet2
        self.wfet3 = wfet3
        self.minwfet1 = minwfet1
        self.minwfet2 = minwfet2
        self.minwfet3 = minwfet3
        self.Buget = Buget # How much money they are CURRENTLY willing to buy at. 
def explain(wealthPoints, prices, budgets, averageWealth, numberBuyers, numberSellers, day, Sellers, Buyers, taxRecord, months):
    q = day - 1 # How many days have passed that there was market activity(This does not include today because the stores never opened)
    plt.plot([x for x in range(q)], wealthPoints, 'b', label = "Collective Coporate Wealth")
    plt.ylabel('Wealth of Market')
    plt.xlabel('Time(days)')
    plt.legend()
    plt.show()
    plt.plot([x for x in range(q)], prices, 'r', label = "Average Prcie")
    plt.plot([x for x in range(q)], budgets, 'g', label = "Average Budget")
    plt.ylabel('Average Market Price')
    plt.xlabel('Time(days)')
    plt.legend()
    plt.show()
    plt.plot([x for x in range(q)], averageWealth, 'b', label = "Average Coparate Wealth")
    plt.ylabel('Average Wealth of Seller')
    plt.xlabel('Time(days)')
    plt.legend()
    plt.show()
    plt.plot([x for x in range(q)], numberBuyers, 'g', label = "Number of Buyers")
    plt.ylabel('Number of Buyers')
    plt.xlabel('Time(days)')
    plt.legend()
    plt.show()
    plt.plot([x for x in range(q)], numberSellers, 'b', label = "Number of Sellers")
    plt.ylabel('Number of Sellers')
    plt.xlabel('Time(days)')
    plt.legend()
    plt.show()
    plt.plot([x for x in range(months)], taxRecord, 'g', label = "Average Taxes")
    plt.ylabel('Average Taxes')
    plt.xlabel('Time(months)')
    plt.legend()
    plt.show()
    names1 = []
    for man in Sellers:
        names1.append((man.id, man.mon, man.price))
    # I'll try this later
    # sellers0 = []
    # pricer = 2-1
    # moneyer = 2-1
    # numberer = 0
    # searcher = []
    # while numberer < len(names1):
    #     pricer += 1
    #     for y in names1:
    #         numberer += 1
    #         if y[2] == pricer:
    #             searcher.append(y)
    #         else:
    #             numberer -= 1
    #             looker = []
    #             xx = 0
    #             taker = 0
    #             while xx < len(searcher):
    #                 moneyer += 1
    #                 for z in searcher:
    #                     xx += 1
    #                     if z[1] == moneyer:
    #                         looker.append(z)
    #                     else:
    #                         taker += 1
    #                 xx -= taker
    #                 sellers0.append(looker)
    #                 looker = []
    # I'll try this later
    names2 = []
    for man in Buyers:
        names2.append((man.id, man.wfet1, man.wfet2, man.wfet3, man.Buget))
    return names1, names2
def taxCode(seller):
    incomeTax = seller.inc * 0.09
    seller.mon -= incomeTax
    wealthTax = seller.mon * 0.05
    seller.mon -= wealthTax
    salesTax = 0
    for sale in seller.trans:
        tax = sale * 0.1
        salesTax += tax
    seller.mon -= salesTax
    propertyValue = (seller.prod.fet1 * 0.5) + (seller.prod.fet2 * 0.8) + (seller.prod.fet3 * 1.2)
    if propertyValue <= 15:
        seller.mon -= 200
    elif propertyValue <= 30:
        seller.mon -= 300
    elif propertyValue <= 45:
        seller.mon -= 500
    elif propertyValue <= 60:
        seller.mon -= 750
    rent = 1500 #May be needed later.
    seller.mon -= rent
    productionCosts = 0
    productionCosts += seller.prod.fet1 * 1.5
    productionCosts += seller.prod.fet2 * 4
    productionCosts += seller.prod.fet3 * 6.25
    seller.mon -= productionCosts
    seller.inc = 0
    seller.trans = []
    return seller
def Street(Buyers, Sellers): 
    OringinalSellers = len(Sellers)
    newBuyer = 1
    newSeller = 1
    numberBuyers = []
    taxRecord = [] 
    numberSellers = []
    failedSellers = [] # A list of sellers that failed to make a profit.
    failedBuyers = [] # A list of buyers that failed to find satifactory products.
    days = 0 # This is used to mesure how many days go on in the month.
    day = 0 # This is used to mesure how many days go on in the market.
    months = 0 # How many months (31 days)have passed in the market
    budgets = [] # A list of average bugets each day.
    averageWealth = [] # A list of average wealth each day.
    wealthPoints = [] # A list of combined money of all stores on every day that has passed in the market.  
    prices = [] # a list of the average price of every day that has passed in the market
    while True: # A loop defineing what happens on a given set of days
        days += 1 # A day starts, needs to be recoreded.
        day += 1 # A day starts, needs to be recoreded.
        if days == 31: # if 31 days have passed since I last asked this question or since we started...
            monthRecord = [] # taxs this month are recorded here.
            for x in Sellers: # Every seller is...
                y = x.mon
                taxCode(x) # ... taxed.
                monthRecord.append(y - x.mon) # taxs this month are recorded here.
                if x.mon < 0: # If they can't affored too...
                    failedSellers.append(("failed to pay taxes", x.id, x.price, day)) # They are added to the failedSellers list with explanation.
                    Sellers.remove(x) # Their evicted.
            taxRecord.append(stats.mean(monthRecord)) # The average tax this month is recorded here.   
            days = 0 # Resets days, justified because we add 1 to months
            months += 1
        if Sellers == []: # If there are no more sellers...
            names1, names2 = explain(wealthPoints, prices, budgets, averageWealth, numberBuyers, numberSellers, day, Sellers, Buyers, taxRecord, months)
            return 'There is no place to buy from.', failedSellers, (len(names2), names2) # And as an added bonus, Tells us what happened
        if months == 600: # After some amount of months...
            names1, names2 = explain(wealthPoints, prices, budgets, averageWealth, numberBuyers, numberSellers, day, Sellers, Buyers, taxRecord, months)
            return (len(names1), names1, failedSellers), (len(names2) ,names2, failedBuyers) # Remaining sellers and buyers
        for b in Buyers: # The buyer walks into the market
            yBug = False # When they check to see if a seller has a good price and they do, This says true.
            # Asks the same thing about the first two fetures fetures
            yfet1 = False
            yfet2 = False
            shuf(Sellers) # Shuffles the sellers so that the buyer can check them in a random order.
            for s in Sellers: # They visit each seller
                if s.quan > 0: # If The selleself has products to sell... 
                    if s.price <= b.Buget: # If The price is right... 
                        yBug = True 
                        #If all three features are right...
                        if s.prod.fet1 >= b.wfet1: 
                            yfet1 = True
                            if s.prod.fet2 >= b.wfet2:
                                yfet2 = True
                                if s.prod.fet3 >= b.wfet3:
                                    s.mon += s.price # Then the Sellers Makes money based on the price
                                    s.inc += s.price # And adds the price to their monthly income tracker
                                    s.trans.append(s.price) # list the value of the transaction  
                                    s.quan -= 1 # There is one less product in inventory
                                    s.vis += 1 # The Seller has made a transaction today
                                    b.Buget = s.price # The buyer wants all products sold to him thereafter at this price. 
                                    b.wfet1 = s.prod.fet1 # The buyer wants all products sold to him thereafter at this quality.
                                    b.wfet2 = s.prod.fet2 # The buyer wants all products sold to him thereafter at this quality.
                                    b.wfet3 = s.prod.fet3 # The buyer wants all products sold to him thereafter at this quality.
                                    break # The buy leaves the market for the day and the next one enters
                                elif Sellers.index(s) == len(Sellers) - 1:# if Feture 3 is universal disatisfying...
                                    b.wfet3 -= 1 # The buyer lowers their standards
                                    if b.wfet3 < b.minwfet3: # If that make the standard 0 or less, they will never return to the market
                                        failedBuyers.append((b.id, b.wfet3, "failed to find a product with a suiltable feature 3", day)) # They are added to the failedBuyers list with explanation. 
                                        Buyers.remove(b)
                                        break    
                            elif yfet2 == False and Sellers.index(s) == len(Sellers) - 1:# if Feture 2 is universal disatisfying...
                                b.wfet2 -= 1 # The buyer lowers their standards
                                if b.wfet2 < b.minwfet2: # If that make the standard 0 or less, they will never return to the market
                                    failedBuyers.append((b.id, b.wfet2, "failed to find a product with a suiltable feature 2", day)) # They are added to the failedBuyers list with explanation. 
                                    Buyers.remove(b)
                                    break
                        elif yfet1 == False and Sellers.index(s) == len(Sellers) - 1: # if Feture 1 is universal disatisfying...
                            b.wfet1 -= 1 # The buyer lowers their standards
                            if b.wfet1 < b.minwfet1: # If that make the standard 0 or less, they will never return to the market
                                failedBuyers.append((b.id, b.wfet1, "failed to find a product with a suiltable feature 1", day)) # They are added to the failedBuyers list with explanation.
                                Buyers.remove(b)
                                break
                    elif yBug == False and Sellers.index(s) == len(Sellers) - 1: # If nobody has a resonable price...
                        b.Buget += 20 # raise buget
                        if b.Buget > b.max: # if this makes the buget bigger than max, check if raising the buget a little less will meet the threshold. if not, the buyer quits.
                            BudAdd = 20 
                            while True:
                                BudAdd -= 5     
                                if BudAdd == 0:
                                    failedBuyers.append((b.id, b.Buget, b.max, "failed to find a product with a suiltable price", day)) # They are added to the failedBuyers list with explanation.
                                    Buyers.remove(b) 
                                    break
                                b.Buget += BudAdd
                                if b.Buget <= b.max:
                                    break
                                else:
                                    b.Buget -= BudAdd
                else: # If there are no products when a seller is visted...
                    if s.prod.price9 * s.cap < s.mon: # If he can afford to, the seller will buy enough products (the price of which is price9)to fill up to capaicty. 
                        s.mon -= s.prod.price9 * s.cap
                        s.inc -= s.prod.price9 * s.cap
                        s.quan = s.cap
                    else: # If he can't afford to...
                        cap1 = s.cap # have a variable take place of s.cap...
                        while True: # lower this number by two and and see if you can afford to fill up to it. do this until the seller finds this is impossible(and go out of buissness) or until reasonable price found.  
                            cap1 -= 2
                            if cap1 <= 0:
                                failedSellers.append(("Cannot afford to restock", s.id, s.price, s.prod.price9, s.cap, s.mon, day))
                                Sellers.remove(s)
                                break
                            if s.prod.price9 * cap1 < s.mon: 
                                s.quan -= s.prod.price9 * cap1    
                                s.quan = cap1
                                break
        for x in Sellers: # If the seller made a transaction today, set the Bollean that checks it to false and raise prices. if not, lower prices. 
            x.price += round(x.vis/30)
            if x.vis == 0:
                x.price -= 5
            x.vis = 0
        MONe = 0 # How much money every seller has combined
        Qmon = [] # the prices of each seller
        bud = [] # the bugets of each buyer
        wealth = [] # the wealth of each seller
        for x in Sellers: 
            MONe += x.mon # The money of all the seller are added up in this variable
            Qmon.append(x.price) # Each sellers price is noted in this 
            wealth.append(x.mon) # Each sellers wealth is noted in this
        for x in Buyers: # The bugets of all the buyers are added up in this variable
            bud.append(x.Buget) # Each buyers price is noted in this list
        wealthPoints.append(MONe) # The wealth of each seller is noted in this list
        averageWealth.append(stats.mean(wealth)) # The average wealth of the market is noted in this list
        budgets.append(stats.mean(bud)) # The mean of the bugets is noted in this lis wealthPoints.append(MONe) # wealthPoints(The list recording market value on any given day) Takes the first vairable
        prices.append(stats.mean(Qmon)) # prices records the average price of the stores that          
        if day % 8 == 0: 
            chance = ri(0, 100) # A random number is generated
            if chance >= 50:
                Buyers.append(Buyer(str(newBuyer) + "nb", ri(3, 12), ri(3, 12), ri(3, 12), ri(50, 450), ri(150, 550), ri(2, 6), ri(2, 6), ri(2, 6))) # A new buyer is added to the market
                newBuyer += 1
            if chance >= 70:
                Buyers.append(Buyer(str(newBuyer) + "nb", ri(3, 12), ri(3, 12), ri(3, 12), ri(50, 450), ri(150, 550), ri(2, 6), ri(2, 6), ri(2, 6))) # A new buyer is added to the market
                newBuyer += 1
            if chance >= 100:
                Buyers.append(Buyer(str(newBuyer) + "nb", ri(3, 12), ri(3, 12), ri(3, 12), ri(50, 450), ri(150, 550), ri(2, 6), ri(2, 6), ri(2, 6))) # A new buyer is added to the market 
                newBuyer += 1
        if day % 5 == 0 and len(Sellers) < OringinalSellers: # If the number of sellers is less than the original number of sellers, a new seller is added to the market
            Dif = OringinalSellers - len(Sellers)
            for x in range(Dif):
                ran = ri(0, 100)
                if ran >= 40:
                    a = ri(3, 12)
                    b = ri(3, 12)
                    c = ri(3, 12)
                    Sellers.append(Seller(str(newSeller) + 'ns', ri(30, 550), ri(10, 20), Product(a, b, c), ri(1000, 15000), ri(10, 40), 0, ri(30, 250), 0, []))
                    if Sellers[-1].min < Sellers[-1].prod.price9:
                        Sellers[-1].min = Sellers[-1].prod.price9 + 10
                    if Sellers[-1].price < Sellers[-1].min: 
                        Sellers[-1].price = Sellers[-1].min + 10  # This is to make sure that the price is always higher than the minimum
                    newSeller += 1
        numberBuyers.append(len(Buyers)) # The number of buyers is noted in this list
        numberSellers.append(len(Sellers)) # The number of sellers is noted in this list
def peopleMaker(Buyers0, Sellers0):
    Buyers = []
    Sellers = []
    for buy in range(0, Buyers0):
        uiteration = str(buy) + "b"
        Buyers.append(Buyer(uiteration, ri(3, 12), ri(3, 12), ri(3, 12), ri(50, 450), ri(150, 550), ri(2, 6), ri(2, 6), ri(2, 6)))
        if Buyers[buy].Buget > Buyers[buy].max:
            Buyers[buy].Buget = Buyers[buy].max - 20
        if Buyers[buy].minwfet1 > Buyers[buy].wfet1:
            Buyers[buy].wfet1 = Buyers[buy].minwfet1
        if Buyers[buy].minwfet3 > Buyers[buy].wfet3:
            Buyers[buy].wfet3 = Buyers[buy].minwfet3
        if Buyers[buy].minwfet2 > Buyers[buy].wfet2:
            Buyers[buy].wfet2 = Buyers[buy].minwfet2
    for sell in range(0, Sellers0):
        a = ri(3, 12)
        b = ri(3, 12)
        c = ri(3, 12)
        uiteration = str(sell) + "s" 
        Sellers.append(Seller(uiteration, ri(30, 550), ri(10, 20), Product(a, b, c), ri(1000, 15000), ri(10, 40), 0, ri(30, 250), 0, []))
        if Sellers[sell].min < Sellers[sell].prod.price9:
            Sellers[sell].min = Sellers[sell].prod.price9 + 10
        if Sellers[sell].price < Sellers[sell].min: 
            Sellers[sell].price = Sellers[sell].min + 10  # This is to make sure that the price is always higher than the minimum   
    return Street(Buyers, Sellers)
People = peopleMaker(800, 80)
print(People) 