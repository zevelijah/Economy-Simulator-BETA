# %%
import matplotlib.pyplot as plt
import statistics as stats
# Note that I explain the variables in the order in wich they are in enabled. To genuinly implement classes, do it in order of __init__ apearence.
# self is not a variable but a self-reference tools that allow you to identify variables via modules of something in that class. Thus all the "self dot"s.
class Product: # This is what is being sold in the market. 
    def __init__(self, fet1, fet2, fet3): #It takes three numbers, represeting different fetures of the prduct.
        self.fet1 = fet1
        self.fet3 = fet3
        self.fet2 = fet2
        self.price9 = fet1 * 2 + fet2 * 3 + fet3 * 6 # What it cost to by the parts from the monopolies that sell them: as a function of the fetures. 
class Seller: # The store.
    def __init__(self, price, quan, prod, mon, cap, vis, min):
        self.min = min # The mininum price the store is willing to sell.
        self.vis = vis # A Boolean asking if a trasaction has been made today. Always starts out False. 
        self.cap = cap # How many product fit in the store.
        self.price = price # The current pricing of their Product. 
        self.quan = quan # How many products they have.
        self.prod = prod #  A Class Product(see above). Sellers are the providers.
        self.mon = mon # How much money I have.
class Buyer: # The Buyer
    def __init__(self, wfet1, wfet2, wfet3, Buget, max):
        self.max = max # The maximum price they are willing to buy at. 
        # Next three variables are the miminum requirements for each feture if they are going to buy it.
        self.wfet1 = wfet1 
        self.wfet2 = wfet2
        self.wfet3 = wfet3
        self.Buget = Buget # How much money they are CURRENTLY willing to buy at. 
def Street(Buyers, Sellers): # Main \_:|_/?
    days = 0 # This is used to mesure how many days go on in the market
    months = 0 # How many months (31 days)have passed in the market
    pricePoints = [] # A list of combined money of all stores on every day that has passed in the market.  
    prices = [] # a list of the average price of every day that has passed in the market
    Test = [] # NOT PERMENANT
    while True: # A loop defineing what happens on a given set of days
        days += 1 # A day starts, needs to be recoreded.
        if days == 31: # if 31 days have passed since I last asked this question or since we started...
            for x in Sellers: # Every seller is...
                x.mon -= 300 # Taxed 300 bucks.
                if x.mon < 0: # If they can't affored too...
                    Sellers.remove(x) # Their evicted.
            days = 0 # Resets days, justified because we add 1 to months
            months += 1
        if Sellers == []: # If there are no more sellers...
            q = (months * 31 + days) - 1 # How many days have passed that there was market activity(This does not include today because the stores never opened)
            # Creates a graph of Market Wealth and Average Market price vs days
            plt.plot([x for x in range(q)], pricePoints, 'b', [x for x in range(q)], prices, 'r') 
            plt.ylabel('Wealth of Market')
            plt.xlabel('Time')
            plt.show()
            return 'There is no place to buy from.', len(Sellers), len(Buyers) # And as an added bonus, Tells us what happened
        if months == 30: # After some amount of months...
            plt.plot([x for x in range(929)], pricePoints, 'b', [x for x in range(929)], prices, 'r') # Do the same thing as if there were no more sellers 
            plt.ylabel('Wealth of Market')
            plt.xlabel('Time')
            plt.show()
            return len(Sellers), len(Buyers) # Remaining sellers and buyers
        for b in Buyers: # The buyers walk into the market
            yBug = False # When they check to see if a seller has a good price and they do, This says true.
            # Asks the same thing about the first two fetures fetures
            yfet1 = False
            yfet2 = False
            for s in Sellers: # They visit each seller
                if s.quan > 0: # If The seller has products to sell... 
                    if s.price <= b.Buget: # If The price is right... 
                        yBug = True 
                        #If all three features are right...
                        if s.prod.fet1 >= b.wfet1: 
                            yfet1 = True
                            if s.prod.fet2 >= b.wfet2:
                                yfet2 = True
                                if s.prod.fet3 >= b.wfet3:
                                    s.mon += s.price # Then the Sellers Makes money based on the price
                                    s.quan -= 1 # There is one less product in inventory
                                    s.vis = True # The Seller has made a transaction today
                                    b.Buget = s.price # The buyer wants all products sold to him thereafter at this price. 
                                    break # The buy leaves the market for the day and the next one enters
                                elif Sellers.index(s) == len(Sellers) - 1:# if Feture 3 is universal disatisfying...
                                    b.wfet3 -= 1 # The buyer lowers their standards
                                    if b.wfet3 <= 0: # If that make the standard 0 or less, they will never return to the market
                                        Buyers.remove(b)
                                        break    
                            elif yfet2 == False and Sellers.index(s) == len(Sellers) - 1:# if Feture 2 is universal disatisfying...
                                b.wfet2 -= 1 # The buyer lowers their standards
                                if b.wfet2 <= 0: # If that make the standard 0 or less, they will never return to the market
                                    Buyers.remove(b)
                                    break
                        elif yfet1 == False and Sellers.index(s) == len(Sellers) - 1: # if Feture 1 is universal disatisfying...
                            b.wfet1 -= 1 # The buyer lowers their standards
                            if b.wfet1 <= 0: # If that make the standard 0 or less, they will never return to the market
                                Buyers.remove(b)
                                break
                    elif yBug == False and Sellers.index(s) == len(Sellers) - 1: # If nobody has a resonable price...
                        b.Buget += 20 # raise buget
                        if b.Buget > b.max: # if this makes the buget bigger than max, check if raising the buget a little less will meet the threshold. if not, the buyer quits.
                            BudAdd = 20 
                            while True:
                                BudAdd -= 5     
                                if BudAdd == 0:
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
                        s.quan = s.cap
                    else: # If he can't afford to...
                        cap1 = s.cap # have a vaiable take place of s.cap...
                        while True: # lower this number by two and and see if you can afford to fill up to it. do this until the seller finds this is impossible(and go out of buissness) or until reasonable price found.  
                            cap1 -= 2
                            if cap1 <= 0:
                                Sellers.remove(s)
                                break
                            if s.prod.price9 * cap1 < s.mon: 
                                s.quan -= s.prod.price9 * cap1    
                                s.quan = cap1
                                break
        for x in Sellers: # If the seller made a transaction today, set the Bollean that checks it to false and raise prices. if not, lower prices. 
            if x.vis == True: 
                x.vis = False
                s.price += 5
            else:
                x.price -= 5
                if x.price < x.min: # keep in mind that when lowered, prices can't be below mininum
                    x.price = x.min
        MONe = 0 # How much money every seller has combined
        Qmon = [] # the prices of each seller
        for x in Sellers: 
            MONe += x.mon # The money of all the seller are added up in this variable
            Qmon.append(x.price) # Each sellers price is noted in this list
        pricePoints.append(MONe) # pricePoints(The list recording market value on any given day) Takes the first vairable
        prices.append(stats.mean(Qmon)) # prices records the average price of the stores that day
        # ,Seller(25, 20, Product(8,2,2), 4000, 25, False, 25)
People = Street([Buyer(5, 0, 0, 300, 300), Buyer(7, 0, 2, 100, 200)],[Seller(30, 10, Product(7, 1, 1), 2500, 15, False, 23),Seller(25, 20, Product(8,2,2), 4000, 25, False, 25),Seller(25, 20, Product(8,2,2), 4000, 25, False, 25)])
print(People)