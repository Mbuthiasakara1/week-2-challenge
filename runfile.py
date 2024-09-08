from customer import Customer
from coffee import Coffee
from order import Order

name1 = Customer("Ryne")
name2 = Customer("Mbuthia")
name3 = Customer ("dinx") 

coffee1 = Coffee("dol")

order1 = Order(name1,coffee1,9.4)
order2 = Order(name1,coffee1,8.0)

print(name1.name)
print(coffee1.name)
print(name1.coffees())
print(coffee1.customers())
print(coffee1.num_orders())
print(coffee1.average_price())