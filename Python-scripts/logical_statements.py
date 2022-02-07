print(""" This program evaluates some statements 
using the logical operators: and, or and not
Statements:
""")
# variables
elephants_can_remember = True
elephants_have_big_ears = True
elephants_can_program_python = False
elephants_can_fly = False
elephants_are_mamals = True
# statements
print("1. Elephants are mamals:" + str(elephants_are_mamals))
print("2. Elephanst can remember:" + str(elephants_can_remember))
print("3. Elephants have big ears:" + str(elephants_have_big_ears))
print("4. Elephants can program in Python:" + str(elephants_can_program_python))
print("5. Elephants can fly:" + str(elephants_can_fly))
print(" ")
# comparisons
print(" Comparison and evaluation of the statement")
print(" ")
print("1. Elephants are mamals and can remember?: " + str(elephants_are_mamals and elephants_can_remember))
print(" ")
print("2. Elephants are mamals and can program in Python?: " + str(elephants_are_mamals and elephants_can_program_python))
print(" ")
print("3. Elephants have big ears or can fly?: " + str(elephants_have_big_ears or elephants_can_fly))
print(" ")
print("4. Elephants cannot fly?: " + str(not elephants_can_fly))
print(" ")
print("5. Elephants do not have big ears?: " + str(not elephants_have_big_ears))
print(" ")
print("6. Elephants can program in Python or can remember?: " + str(elephants_can_program_python or elephants_can_remember))
print(" ")

