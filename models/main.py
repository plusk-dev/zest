from pony.orm import *
from datetime import datetime
database = Database()


class User(database.Entity):
    username = Required(str, unique=True)
    password = Required(str)
    display_name = Required(str)
    admin = Required(bool)

class Order(database.Entity):
    name = Required(str)
    date = Required(datetime)
    data = Required(Json)

# class Estimate(database.Entity):
#     pass

# class Product(database.Entity):
#     pass

# class Section(database.Entity):
#     pass

# class Part(database.Entity):
#     pass