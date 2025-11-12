class Restaurant:
    name = ''
    category = ' '
    rating = 0.0
    delivery = False


bob = Restaurant()

bob.name = "Bob\'s Burger"
bob.category = "American Diner"
bob.rating = 4.7
bob.delivery = False

print(vars(bob))

