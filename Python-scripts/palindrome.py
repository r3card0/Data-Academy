# evaluates a string to determines if is a palindrome
# 1 user enter the string
# preparation
# evaluation
# answer

def palindrome():
    # 1 user enter the string
    word_phrase = str(input("Enter a word or phrase: "))    
    # 2 eliminates spaces, transforms all words in lowercase
    word_phrase = word_phrase.strip() 
    word_phrase = word_phrase.lower()
    # , compare reverse 
    if word_phrase == word_phrase[::-1]:
        print("Is a palindrome")
    else:
        print("Is not a palindrome")

if __name__ == "__main__":
    palindrome()


