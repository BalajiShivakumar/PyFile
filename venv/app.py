import ecommerce.shipping
#ecommerce.shipping.calc_shipping()

# or

from ecommerce.shipping import calc_shipping
#calc_shipping()


import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))


members = ["Balaji", "Aswin", "Manohar", "Praveen", "Surya"]
leader = random.choice(members)
print(leader)
