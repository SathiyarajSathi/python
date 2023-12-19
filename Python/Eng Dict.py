import json
from difflib import get_close_matches

data=json.load(open("E:\OLD PC\Python\flow.json"))
user_word=input("Enter a word: ")

def meaning(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0]
        print("Did you mean {}. If yes type (y) else type (n)".format(close_match.title()))
        choice = input()
        choice = choice.lower()
        if choice == "y":
            print(close_match)
            return data[close_match]
        elif choice == "n":
            return "Sorry, We can't find."
        else:
            return "Invalid entry."
        
    else:
        return "Word didn't exist!"


definition = meaning(user_word)
print(definition)
