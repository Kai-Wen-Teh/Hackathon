import math
import random
    
shops = []

#ZS
def add_shop(shop_instance, ):
    shops.append(shop_instance)

#ZS
def check_shop_image(shop_name):
    for i in shops:
        if shop_name in i.name:
            shop = i
            break
    return shop.image

def check_shop_status(shop_name):
    for i in shops:
        if shop_name in i.name:
            shop = i
            break
    return shop.status

#ZS
def shops_within_range(radius):
    # location = locate()
    # we dont really know how to implement this so we use sample to simulate it.
    shops_name = []
    shop_sample = random.sample(shops, 5)
    for i in shop_sample:
        shops_name.append(i.name + ", " + i.status)
    return shops_name

#ZS
def shows_open_only():
    shops_name = []
    for i in shops:
        if i.status == "O":
            shops_name.append(i.name)
    return shops_name
    
class Shop:

    description = ""
    name = ""
    image = ""
    open_or_closed = ""
    location = ""

    def __init__(self, name, description, image, location):
        self.description = description
        self.name = name
        self.image = image
        self.status = "C"
        open_or_closed = input("Is your shop open? (Type O for open, C for closed): ").upper()
        if open_or_closed == "O":
            self.status = "O"
        self.open_or_closed = open_or_closed
        self.location = location

        




