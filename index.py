import random
import json

f = open('vocab-files\\french.json', "r+", encoding='utf8')

french_vocab = json.load(f)

subject = input('Enter a subject: ')
f = open(f'vocab-files\\{subject}.json', encoding='utf8')
vocabulary = json.load(f)

def addVocabulary(vocabulary: dict, word: str, meaning: str):
    vocabulary[word] = meaning
    return vocabulary

while True:
    word = input('new vocabulary: ')
    if word != 'X':
        meaning = input('meaning: ')
        addVocabulary(vocabulary, word, meaning)
    else: break