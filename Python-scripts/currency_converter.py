# runs currency convertion
# convert from colombian pesos to dollars

pesos = int(input("How many colombian pesos 💰 do you have?: "))
pesos = float(pesos)
dollar_price = 4011.65
dollars = round(pesos/dollar_price,2)
dollars = str(dollars)

print("You have $" + dollars + " dollars")
print("Thanks 😀 ")