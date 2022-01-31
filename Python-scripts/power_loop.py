


def welcome_message():
    print(""" 
    This program calculates the power of numbers.
    You can choose the exponent value and ...
    You can chose the limit of the calculations
    """)

welcome_message()

def input_values():
    # print(welcome_message())
    # base_number = int(input("Please, enter the base value: "))
    exponent_number = int(input("Enter the exponent value:"))
    print(" ")
    limit_number = int(input("Enter the limit value of the calculations: "))
    
    # base value
    base_number = 0
    
    # loop
    while base_number < limit_number:
        # base_number = base_number + 1
        base_number += 1
        power_of = base_number ** exponent_number
        print("The power " + str(exponent_number) + " of " + str(base_number) + " is: " + str(power_of))


if __name__ == "__main__":
    input_values()

    

