from time import sleep

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def countwords(file):
    splut = file.split()
    words = 0
    for word in splut:
        words += 1
    return words

def countletters(content):
    dict = {}
    for character in content:
        if character.lower() not in dict:
            dict[character.lower()] = 1
        else:
            dict[character.lower()] += 1
    return dict

def report(dict_letters):
    print("==== Begin report ====")
    english_letters = {}
    for entry in dict_letters:
        if entry in letters:
            if entry not in english_letters:
                english_letters[entry] = dict_letters[entry]
    for total in english_letters:
        print("The '" + total + "' character was found " + str(dict_letters[total]) + " times")


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    report(countletters(file_contents))
