# runs currency convertion
# convert from colombian pesos to dollars

pesos = int(input("How many colombian pesos 💰 do you have?: "))
pesos = float(pesos)
dollar_price = 4011.65
dollars = round(pesos/dollar_price,2)
dollars = str(dollars)

print("You have $" + dollars + " dollars")
print("Thanks 😀 ")

## convert from mexican pesos to dollars

pesos = int(input("How many mexican pesos 💰 do you have?: "))
pesos = float(pesos)
dollar_price = 21.4
dollars = round(pesos/dollar_price,2)
dollars = str(dollars)

print("You have $" + dollars + " dollars")
print("Thanks 😀 ")

## convert from dollars to mexican pesos

dollars = int(input("How many dollars 💰 do you have?: "))
dollars = float(dollars)
dollar_price = 21.4
pesos = round(dollars * dollar_price,2)
pesos = str(pesos)

print("You have $" + pesos + " mexican pesos")
print("Thanks 😀 ")