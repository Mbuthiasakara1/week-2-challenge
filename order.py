
class Order:
    all =[]
    def __init__(self,customer,coffee,price): 
        from customer import Customer
        from coffee import Coffee 
        
        if not isinstance(customer,Customer):
            raise Exception("customer must be an instance of Customer class")
        if not isinstance(coffee,Coffee):
            raise Exception("coffee must be an instance of Coffee class")
        self.customer =customer
        self.coffee = coffee

        if isinstance (price,float) and  1.0 <= price <=10.0:
            self.price =price

        else:
            raise TypeError ("The price must be a float btn 1.0 to 10.1") 
        Order.all.append(self)
