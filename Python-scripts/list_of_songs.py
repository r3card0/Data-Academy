# List of songs
def show_message():
    print(""" 
    This program concatenates two lists of songs 🎤🎧🎼🎹
    """)

show_message()

def concatenate_lists():
    list_songs = ["Born to be ready", "Waste", "Remember Me", "Slow Burn"] 
    list_songs2 = ["Taste of you", "Lazy Baby", "We Belong", "After we collied", "So good"] 
    all_songs = list_songs + list_songs2

    print("List 1:" + str(list_songs) + " 🎸")
    print("List 2:" + str(list_songs2) + " 🪗")
    print(" ")
    print("The union of the lists is 🎼 : " + str(all_songs) + " 🎺")

if __name__ == "__main__":
    concatenate_lists()