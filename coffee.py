from order import Order
class Coffee:
    all=[]
    def __init__(self,name):
        if isinstance(name,str) and len(name) in range (1,4):
            self.name =name

        else:
            raise TypeError ("The name should be a string in a 3 character")    

        Coffee.all.append(self)


    def orders(self):
        return [order for order in Order.all if order.coffee == self]#list of all the instances pf that specific coffee containing price and customer name.[kalvine,moc,3.4],[kalvine,moc,3.4]
    def customers(self):
        return [order.customer.name for order in self.orders()]#list of the above method self.orders.
    def num_orders(self):
        total = 0
        for order in self.orders():
            total +=1
        return total    

    def average_price(self):
        prices = [order.price for order in self.orders()]#[2.4,5.6,4.5.6.7]
        total_price = sum(prices)#[34]
        average_price =total_price/len(prices)#[34/4]

        return average_price