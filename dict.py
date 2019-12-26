import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def  translate(word):
    word  = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())):
        yn = input("Did you mean %s Instead? Enter Y if yes, or N if  no:  " % get_close_matches(word,data.keys())[0])
        if yn.lower() == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn.lower() == 'n':
              return "The word doesn't exist in Dictionary. Please double check it!"
        else : 
              return "We didn't understant your choice!"
    else:
        return "The word doesn't exist in Dictionary. Please double check it!"

word = input("Enter the word:   ")

output = translate(word)
if  type(output) == list:
    print("\n\nThe word  means: \n")
    for item in output:
        print("- ",item)
else:
    print("\n No result found: ",translate (word))