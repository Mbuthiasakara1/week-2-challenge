from order import Order

class Customer:
    all =[]

    def __init__(self,name):
        if isinstance (name,str) and  len(name) in range (1,16):
             self.name=name
             
        else:
            raise TypeError ("The name should be a string of a 15 characters")          
        Customer.all.append(self)

    def orders(self):
        return [order for order in Order.all if order.customer== self]#list of all orders made by the specific customer.[kalvine,moc,3.4],[kalvine,moc,3.4],[kalvine,moc,3.4],
    
    def coffees(self):
        return [order.coffee.name for order in self.orders()]# list of all the coffe names ordered by the specific customer.[moc,moc,moc]
    
    def create_order(self,coffee,price):
        Order(self,coffee,price)# it is connecting our customer class to the coffee thru the order# create an instance of the order class
