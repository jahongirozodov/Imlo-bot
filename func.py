from uzwords import words
from difflib import get_close_matches

# print(get_close_matches('содир',words))

def checkword(word, words = words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    avaible = False
    if word in matches:
        avaible = True
        matches = word
    elif 'x' in word:
        word = word.replace('x','ҳ')
        matches.update(get_close_matches(word,words))
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'x')
        matches.update(get_close_matches(word,words))
    return {'avaible': avaible, 'word': matches}


if __name__== '__main__':
    print(checkword('xайрат'))
