class Prices:
    max_price = 20


    def __init__(self, make, taste,size, price=0):
        self.make = make
        self.taste = taste
        self.size = size
        self.price = price


    def increase(self, increases):
        if self.price + increases <= Prices.max_price:
            self.price += increases 
        else:
            self.price = Prices.max_price


    def get_price(self):
        return self.price
    
price1 = Prices("Ciel", "Water", "Medium")
price2 = Prices("Coke", "Coke", "Small")

# Increase the price
price1.increase(1)
price2.increase(2)

#print the current price
print(f"{price1.make} {price1.taste} {price1.size} the actual price of {price1.get_price()} usd.")
print(f"{price2.make} {price2.taste} {price2.size} the actual price of {price2.get_price()} usd.")
