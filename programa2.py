import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Vc digitou %s ? enter Y yes or N no" % get_close_matches(w ,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "A palavra nao existe"
        else:
            return "Entrada invalida"
    else:
        return "The word does not exist"

word = input('Enter the word:')
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)