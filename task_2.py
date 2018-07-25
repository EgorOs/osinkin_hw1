#!/usr/bin/env python3

def FindFrequentWord(usr_input):
    # Remove punctuation to avoid situations, when punctuation marks stick to words
    usr_input = usr_input.replace(',', '').replace('.', '').replace('?', '').replace('!', '')
    words = usr_input.split()
    vocabulary = {}
    max_count = 1
    frq_words = []
    for w in words:
        if not vocabulary.get(w):
            vocabulary[w] = 1
        else:
            vocabulary[w] += 1
            if vocabulary[w] > max_count:
                max_count = vocabulary[w]
                frq_words = [w]
            elif vocabulary[w] == max_count:
                frq_words.append(w)

    return frq_words, max_count

while True:
    # Setting input string as a lowercase to avoid case sensetivity
    usr_input = input("Type anything:\n").lower()
    if usr_input == "cancel":
        break
    else:
        res, num = FindFrequentWord(usr_input)
        for i in res:
            print('{} - {}'.format(num, i))
