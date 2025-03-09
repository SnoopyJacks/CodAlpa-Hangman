import requests
import random

"""Get word from API"""
def get_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        response.raise_for_status()
        word =response.json()[0]
        return word.lower()
    except requests.exceptions.RequestException:
        return random.choice(["dog", "cat", "wolf", "rat"])
    
"""print(get_random_word()) to test function 1"""
    
"""Display letter/Word"""
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

"""word = get_random_word()
print(display_word(word, set()))
function 2 test"""
        
"""game function"""
def hangman():
    word =get_random_word()
    guessed_letters = set()
    attempts = 15
    
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters)) #blank word
    
    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter")
            continue
        
        guessed_letters.add(guess)  #next guess
        
        if guess in word:
            print("Correct")
        else:
            attempts -= 1
            print(f"Sorry, that is incorrect. You have {attempts} attempts left")
            
        print(display_word(word, guessed_letters)) #updates display
        
        if "_" not in display_word(word, guessed_letters):
            print("\n Congratulations. The word was", word )
            break
        
    else:
        print("\n Sorry! The word was", word)
        
if __name__=="__main__":
    hangman()