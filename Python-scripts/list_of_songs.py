# List of songs
def show_message():
    print(""" 
    This program concatenates two lists of songs π€π§πΌπΉ
    """)

show_message()

def concatenate_lists():
    list_songs = ["Born to be ready", "Waste", "Remember Me", "Slow Burn"] 
    list_songs2 = ["Taste of you", "Lazy Baby", "We Belong", "After we collied", "So good"] 
    all_songs = list_songs + list_songs2

    print("List 1:" + str(list_songs) + " πΈ")
    print("List 2:" + str(list_songs2) + " πͺ")
    print(" ")
    print("The union of the lists is πΌ : " + str(all_songs) + " πΊ")

if __name__ == "__main__":
    concatenate_lists()