import shop_checker
import shop_side
import customer_side

#show shops within 10km
shop_checker.shops_within_range(10)

name = input("enter a shop name to see the image: ")

#check shop image based on the name
shop_checker.check_shop_image(name)