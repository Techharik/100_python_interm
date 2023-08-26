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

insuffient_order =False
today_income = 0

def report(qty):
        print(f"The available resources water :- {qty['water']} milk:- {qty['milk']} coffee:- {qty['coffee']} .")


def update_report(flav):
        if flav == 'cappuccino':
            resources["water"] -= MENU['cappuccino']['ingredients']['water']
            resources["milk"] -= MENU['cappuccino']['ingredients']['milk']
            resources["coffee"] -= MENU['cappuccino']['ingredients']['coffee']
            report(resources)
        if flav == 'espresso':
            resources["water"] -= MENU['espresso']['ingredients']['water']
            resources["coffee"] -= MENU['espresso']['ingredients']['coffee']
            report(resources)

        if flav == 'latte':
            resources["water"] -= MENU['latte']['ingredients']['water']
            resources["milk"] -= MENU['latte']['ingredients']['milk']
            resources["coffee"] -= MENU['latte']['ingredients']['coffee']
            report(resources)

def check_resources(flav):
        if flav == 'cappuccino':
                if resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources["milk"] >= MENU['cappuccino']['ingredients']['milk'] and resources["coffee"] >= MENU['cappuccino']['ingredients']['coffee'] :
                    return True
                else:
                    print(f'insufficient resources')
                    return False
                
        elif flav == 'espresso':
                if resources['water'] >= MENU['espresso']['ingredients']['water'] and  resources["coffee"] >= MENU['espresso']['ingredients']['coffee'] :
                    return True
                else:
                    print(f'insufficient resources')
                    return False
                
        elif flav == 'latte':
                
                if resources['water'] >= MENU['latte']['ingredients']['water'] and resources["milk"] >= MENU['latte']['ingredients']['milk'] and resources["coffee"] >= MENU['latte']['ingredients']['coffee'] :
                    return True
                else:
                    print(f'insufficient resources')
                    return False

def update_income(amt):
             global today_income
             today_income += amt

def order(amt,flav):
        global insuffient_order

        if flav == 'cappuccino':
            available_res = check_resources(flav)
            print(available_res)
            if available_res == True:
                if(amt >= MENU['cappuccino']['cost']): 
                    print(f'Prearing {flav}')
                    update_report(flav)
                    update_income(amt)

                    print(f'Take your coffee happy day!')
                else:
                    print(f"print insufficient amount - {amt}")
            else:
                
                report(resources)
                print('Make order according to the availablity')
                insuffient_order = True

        if flav == 'espresso':
            available_res = check_resources(flav)
            print(available_res)
            if available_res == True:
                if(amt >= MENU['espresso']['cost']): 
                    print(f'Prearing {flav}')
                    update_report(flav)
                    update_income(amt)
                    print(f'Take your coffee happy day!')
                else:
                    print(f"print insufficient amount - {amt}")
            else:
                
                report(resources)
                print('Make order according to the availablity')
                insuffient_order = True

        if flav == 'latte':
            available_res = check_resources(flav)
            print(available_res)
            if available_res == True:
                if(amt >= MENU['latte']['cost']): 
                    print(f'Prearing {flav}')
                    update_report(flav)
                    update_income(amt)
                    print(f'Take your coffee happy day!')
                else:
                    print(f"print insufficient amount - {amt}")
            else:
               
                report(resources)
                print('Make order according to the availablity')
                insuffient_order = True
            
            
        


            
def order_cash():
        quarters =int(input('How many quarter?'))
        dimes =int(input('How many dimes?'))
        nickel =int(input('How many nickel?'))
        pennies =int(input('How many pennies?'))

        total= (quarters * 0.25)+(0.1*dimes)+(0.05*nickel)+(0.01* pennies)
        print(f'your total amount is {total}')
        return total

while not insuffient_order:
    flavours = input("What kind of coffee do you want to consume?")

    def making_coffee(flav):
        if flav == 'report':
            return report(resources)
        elif flav == 'cappuccino':
            choosen_flav = MENU['cappuccino']['ingredients']
            amount = order_cash()
            order(amount,flav)
        elif flav == 'espresso':
            choosen_flav = MENU['espresso']['ingredients']
            amount = order_cash()
            order(amount,flav)
        elif flav == 'latte':
            choosen_flav = MENU['latte']['ingredients']
            amount = order_cash()
            order(amount,flav)
        elif flav == 'admin':
             print(f"Here is the income chief {today_income}")
        else:
             print('Ivalid flavvours')

    making_coffee(flavours)