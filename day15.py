'''#? Building a coffee machines '''
print('Hello')
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report(qty):
    print(f"The available resources water :- {qty['water']} milk:- {qty['milk']} coffee:- {qty['coffee']} .")

flavours = input("What kind of coffee do you want to consume?")

def order(amt,flav):
    if flav == 'cappuccino':
        if(amt)      
 


def making_coffee(flav):
    if flav == 'report':
        return report(resources)
    elif flav == 'cappuccino':
        choosen_flav = MENU['cappuccino']['ingredients']
        print(f'Prearing {flav}')
        order()

making_coffee(flavours)