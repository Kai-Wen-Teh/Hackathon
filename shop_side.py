import shop_checker

# create 10 fake sample shops

for i in range(10):
    name = "shop" + str(i)
    description = "description" + str(i)
    image = "image" + str(i)
    location = "location" + str(i)
    shop_checker.add_shop(shop_checker.Shop(name, description, image, location))


    

