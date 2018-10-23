"""Creates a gematria dictorary for the nltk corpus of words, and allows
any entered word to get a gematria value. This algorithm takes much longer
as it creates an entire gematria dictionary. Runtime may improve by just
doing a case by case calculation"""

import nltk
import random
from nltk.corpus import words


letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
    'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
    'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7,
     '-':0, '\'':0}

def gematria(word):
    #Gives gematria value for individual inputted word
    value = 0
    word = word.lower()
    for letter in word:
        value += letter_vals[letter]
    return value


def satan_words(text):
    #Finds total words in a text with a value of 666
    total = 0
    text = text.split()
    for word in text:
        if gematria(word) == 666:
            total += 1
            print(word)
    return total

gemdict = {}
for w in words.words():
    w = w.lower()
    gemdict[gematria(w)] = w


def decode(text):
    print('Original text: ',text)
    #Replaces a random amount of words in the text with their gematria values
    text = text.split(' ')
    numreplaced = random.randint(0,len(text))
    for n in range(numreplaced):
        val = random.randint(0, (len(text)-1)) #Val is the index to be replaced
        if isinstance(text[val], int):
            continue
        text[val] = gematria(str(text[val]))
        text[val] = gemdict[text[val]]
        
    sentence = ' '.join(str(x) for x in text)
    return('Gematrified: ',sentence)

myword = input("Enter a word to find its gematria value: ")
print(gematria(myword))



