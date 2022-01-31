print(""" 
This program lets you know if your choosen number for 'Y' is grater than or less than  the value of 'X'
- If the value of 'Y' is greater than 'X' value, returns: True 
- If the value of 'Y' is lower than 'X' value, returns: False 
""")

Y = int(input("Is 'Y' value greater than 'X' value?. Choose 'Y' value: "))
X = 2500
if Y > X:
    print(True)
else:
    print(False)