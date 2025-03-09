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
    
print(get_random_word())
        