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
    attempts = 7
    
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters)) #blank word
    
    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()