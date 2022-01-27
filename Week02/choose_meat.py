# usar if, elif, else
# operadores logicos
# funciones
# usa¡uario elija un menu
# huevos con jamon o con tocino
# menu con las opciones jamon o tocino
# variable ingredient

# bacon = "bacon"
# jam = "jam"
# both = "bacon and jam"

# menu = int(input("""
# We offer you eggs  as breakfast and you can add
# and extra ingredient

# Bacon       (1)
# Jam         (2)
# BAcon & Jam (3)

# Please, choose an option!: """))

# if menu == 1:
#     print("Your order is: Eggs with " + bacon)
# elif menu == 2:
#     print("Your order is: Eggs with " + jam)
# elif menu == 3:
#     print("Your order is: Eggs with " + both)
# else:
#     print("Choose a correct option")

def choose(ingredient):
    print("Your order is: Eggs with " + ingredient)

def run():
    bacon = "bacon 🍳 🥓"
    jam = "jam 🍳🍖"
    both = "bacon and jam 🍳🥓🍖"

    menu = int(input("""
    We offer you eggs 🥚🍳 as a breakfast and you can add
    and extra ingredient

    Bacon 🥓            (1)
    Jam   🍖            (2)
    Bacon & Jam 🥓 🍖   (3)

    Please, choose an option!: """))

    if menu == 1:
        choose(bacon)
    elif menu == 2:
        choose(jam)
    elif menu == 3:
        choose(both)
    else:
        print("Choose a correct option")
    

if __name__ == "__main__":
    run()

