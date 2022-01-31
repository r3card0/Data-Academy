# runs currency with 3 menus of option

def currencies_to_dollars(pesos, dollar_price):
    local_currency = int(input("How many $ " + pesos + " do you have: "))
    local_currency = float(local_currency)
    dollars = str(round(local_currency/dollar_price, 2))
    print("You have $" + dollars + " dollars")
    print("Thanks 😀 ")

def currencies_to_dollars_menu():
    menu_currencies = int(input(""" 
    Mexican pesos       (1)
    Colombian pesos     (2)
    Argentine pesos     (3)

    Please! Choose an option: """))

    if menu_currencies == 1:
        currencies_to_dollars("mexican pesos", 21.5)
    elif menu_currencies == 2:
        currencies_to_dollars("colombian pesos", 4500.1)
    elif menu_currencies == 3:
        currencies_to_dollars("argentine pesos", 102)
    else:
        print("Please! Select a correct option")

def dollars_to_currencies(dollar_price,pesos):
    dollars_amount = int(input("How many dollars 💰 do you have?: "))
    dollars_amount = float(dollars_amount)    
    dollars_to_local_currency = str(round(dollars_amount * dollar_price,2))
    print("You have: $" + dollars_to_local_currency +  " " + pesos)
    print("Thanks 😀 ")

def dollars_to_currencies_menu():
    menu_dollars = int(input(""" 
    Dollars to mexican pesos       (1)
    Dollars to colombian pesos     (2)
    Dollars to argentine pesos     (3)

    Please! Choose an option: """))

    if menu_dollars == 1:
        dollars_to_currencies(21.5,"mexican pesos")
    elif menu_dollars == 2:
        dollars_to_currencies(4500,"colombian pesos")
    elif menu_dollars == 3:
        dollars_to_currencies(102,"argentine pesos")
    else:
        print("Please! Select a correct option")

def main_mennu():
    main_menu = int(input(""" 
    Dollars to other currency   (1)
    Currencies to dollars        (2)

    Please! Choose one option: """))

    if main_menu == 1:
        print(dollars_to_currencies_menu())
    elif main_menu == 2:
        print(currencies_to_dollars_menu())
    else: 
        print("Please! Select a correct option")

if __name__ == "__main__":
    main_mennu()


# pesos = int(input("How many colombian pesos 💰 do you have?: "))
# pesos = float(pesos)
# dollar_price = 4011.65
# dollars = round(pesos/dollar_price,2)
# dollars = str(dollars)

# print("You have $" + dollars + " dollars")
# print("Thanks 😀 ")

# ## convert from mexican pesos to dollars

# pesos = int(input("How many mexican pesos 💰 do you have?: "))
# pesos = float(pesos)
# dollar_price = 21.4
# dollars = round(pesos/dollar_price,2)
# dollars = str(dollars)

# print("You have $" + dollars + " dollars")
# print("Thanks 😀 ")

# ## convert from dollars to mexican pesos

# dollars = int(input("How many dollars 💰 do you have?: "))
# dollars = float(dollars)
# dollar_price = 21.4
# pesos = round(dollars * dollar_price,2)
# pesos = str(pesos)

# print("You have $" + pesos + " mexican pesos")
# print("Thanks 😀 ")

# 1 crear menu de eleccion
# 2 crear las condiciones repetitivas
# 3 parametros y argumentos