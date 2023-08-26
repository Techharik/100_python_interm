''' OBJECT ORIENTED PROGRAMMING  '''

#? OBJECT  - DATA AND FUNTION NORMALLY WE CAN SAY ATTRIBUTES AND METHODS, HAS AND DOES

#? CLASS - BLUE PRINT TO CREATA A OBJECTS: generate as many object you have

# ! class are captilized:
# Exammple:
# from turtle import *
# color('red','yellow')
# begin_fill()

# while True:
#     forward(500)
#     left(170)
#     if abs(pos()) <1:
#         break
# end_fill()
# done()


#!  using external package using pip 

# from prettytable import PrettyTable
# table = PrettyTable()

# table.field_names = ["Pokemon", "combat",]
# table.add_row(["pickachu", "eletric"])
# table.add_row(["richu", "electric"])
# table.add_column("alive",["yes", "no"])
# table.align = 'l'

# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

money_machine = MoneyMachine()
cofee_maker = CoffeeMaker()

money_machine.report()
cofee_maker.report()

is_on = True


while is_on:
    options =menu.get_items()
    flavour = input('What is your flavour?({options})')
    
    if flavour == 'off':
        is_on:False
    elif flavour == 'report':
        cofee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(flavour)
        if cofee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
             cofee_maker.make_coffee(drink)


                



