
def supermarket_list():
    vegetables = ["🍅", "🥦", "🫒", "🥬", "🥒", "🌶", "🧄"]
    fruits = ["🍎", "🍇", "🍒", "🍍", "🥥"]
    meat = ["🥩", "🍗", "🍖"]

    print("This is the supermarket list:")
    print(" 1. Vegetable's list" + str(vegetables))
    print(" 2. Fruit's list" + str(fruits))
    print(" 3. Meat's list" + str(meat))
    print(" ")

    def classify():
        # Classify by color
        print("Classify by color:")
        red_ones = str(vegetables[0]) + ", " + str(vegetables[5]) + ", " + str(fruits[0]) + ", " + str(fruits[2]) + ", " + str(meat[0])
        green_ones = vegetables[1:4]
        print("- Red ones: " + str(red_ones))
        print("- Green ones: " + str(green_ones))
        print(" ")
    
    classify()

    def add_items():
        print("Add more fruits:")
        fruits.append("🍌")
        fruits.append("🍉")
        print("- Add 🍌 to fruit list:" + str(fruits))
        print(" ")

    add_items()

    def eliminate_items():
        print("Eliminate garlic:")
        no_garlic = vegetables.pop(6)
        print("- No more garlic: " + str(no_garlic) + " " + str(vegetables))
    
    eliminate_items()

if __name__ == "__main__":
    supermarket_list()
