'''Project 1: Rosalind Kidwell, Ricki DiCristoforo, Drew Pearson
This project attempts to distinguish between animals and people using common
features of their surrounding words. 
'''

import nltk
from nltk.corpus import brown
from nltk import pos_tag

browntext = brown.words()
#fdist = nltk.FreqDist(w.lower() for w in browntext) <-- this didn't work

animals = ['aardvark', 'algae', 'alpaca', 'ameoba', 'anteater', 'ape', 'aphid', 'arachnid',
           'armadillo', 'asp', 'alligator', 'ant', 'baboon', 'badger', 'bat', 'bear', 'bee', 'bird', 'camel','cat', 'dog',
           'butterfly', 'bumblebee', 'bulldog', 'bull','bug', 'caribou', 'cheetah', 'chicken', 'chimpanzee', 'cow', 'crocodile', 'deer',
           'dolphin', 'duck', 'eagle', 'elephant', 'fish', 'fly', 'fox',
           'frog', 'giraffe', 'goat', 'goldfish', 'hamster', 'hippopotamus',
           'horse', 'kangaroo', 'kitten', 'lion', 'lobster', 'monkey', 'owl',
           'octopus', 'panda', 'peacock', 'pig', 'pony','puppy', 'rabbit', 'rat', 'scorpion',
           'seal', 'shark', 'sheep', 'snail', 'snake', 'spider', 'squirrel',
           'tiger', 'turtle', 'wolf', 'zebra']
from nltk.corpus import names
malenames = names.words('male.txt')
femalenames = names.words('female.txt')
people = ['he', 'she', 'people', 'person'] + malenames + femalenames #Change to all names

pprevword = []
ppostword = []
aprevword = []
apostword = []

animalpos = []
peoplepos = []
for w in range(len(browntext)):
    if browntext[w] in people:
        pprevword.append(browntext[w-1])
        ppostword.append(browntext[w+1])

        test = browntext[w].split(' ')
        pos = nltk.pos_tag(test)
        peoplepos.append(pos)

    if browntext[w] in animals:
        aprevword.append(browntext[w-1])
        apostword.append(browntext[w+1])

        test = browntext[w].split(' ')
        pos = nltk.pos_tag(test)
        animalpos.append(pos)

from collections import Counter

ppos = []
for pair in peoplepos:
    ppos.append(pair[0][1])

apos = []
for pair in animalpos:
    apos.append(pair[0][1])
    
apos = Counter(apos)
ppos = Counter(ppos)

print('The most common parts of speech for people are: ', ppos.most_common(15), '\n')
print('The most common parts of speech for animals are: ', apos.most_common(15), '\n')

distinctpprevword = []
distinctppostword = []
distinctaprevword = []
distinctapostword = []

for w in pprevword:
    if w not in aprevword:
        distinctpprevword.append(w)
distinctpprevword = Counter(distinctpprevword)

for w in ppostword:
    if w not in apostword:
        distinctppostword.append(w)
distinctppostword = Counter(distinctppostword)

for w in aprevword:
    if w not in pprevword:
        distinctaprevword.append(w)
distinctaprevword = Counter(distinctaprevword)

for w in apostword:
    if w not in ppostword:
        distinctapostword.append(w)
distinctapostword = Counter(distinctapostword)


pprevword = Counter(pprevword)
ppostword = Counter(ppostword)
aprevword = Counter(aprevword)
apostword = Counter(apostword)


print('The most common words preceding people are: ', pprevword.most_common(20),'\n')
print('The most common words preceding animals are: ', aprevword.most_common(20), '\n')
print('The most common words following people are: ', ppostword.most_common(20), '\n')
print('The most common words following animals are: ', apostword.most_common(20), '\n')


print('The most common words that are not found before animals, but are before people are: ', distinctpprevword.most_common(15), '\n')
print('The most common words that are not found after animals, but are after people are: ', distinctppostword.most_common(15), '\n')
print('The most common words that are not found before people, but are before animals are: ', distinctaprevword.most_common(15), '\n')
print('The most common words that are not found after people, but are after animals are: ', distinctapostword.most_common(15), '\n')

        
        
