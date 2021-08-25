import math
import random
    
shops = []

def add_shop(shop_instance, ):
    shops.append(shop_instance)

def clear_shops():
    shops = []

def check_shop_image(shop_name):
    res = "could not find the shop"
    for i in shops:
        if shop_name in i.name:
            shop = i
            res = shop.image
            break
    return res

def check_shop_status(shop_name):
    res = "could not find the shop"
    for i in shops:
        if shop_name in i.name:
            shop = i
            res = shop.status
            break
    return res

def shops_within_range(radius):
    # location = locate()
    # we dont really know how to implement this so we use sample to simulate it.
    shops_name = []
    shop_sample = random.sample(shops, 5)
    for i in shop_sample:
        shops_name.append(i.name + ", " + i.status)
    return shops_name

def shows_open_only():
    shops_name = []
    for i in shops:
        if i.status == "O":
            shops_name.append(i.name)
    return shops_name

def case_nearby_the_shop(shop_name, MySejahtera_api = None):
    #simulate case nearby for each shop
    case = []
    for i in range(0, 10):
        case.append(random.randint(0, 200))
    res = "could not find the shop."
    shops_name = []
    for i in range(len(shops)):
        if shop_name == shops[i].shop_name:
            res = case[i]
            break
    return res


        
class Shop:

    description = ""
    name = ""
    image = ""
    status = ""
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




