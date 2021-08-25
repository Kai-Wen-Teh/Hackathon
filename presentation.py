import shop_checker

test = shop_checker.Shop("name", "description", "image", "location")
shop_checker.add_shop(test)

shop_checker.clear_shops()

# create 10 fake sample shops
for i in range(10):
    name = "shop" + str(i)
    description = "description" + str(i)
    image = "image" + str(i)
    location = "location" + str(i)
    shop_checker.add_shop(shop_checker.Shop(name, description, image, location))

#show shops within 10km
shop_checker.shops_within_range(10)

name = input("enter a shop name to see the image: ")

#check shop image based on the name
shop_checker.check_shop_image(name)

#check shop status based on the name
shop_checker.check_shop_status(name)
