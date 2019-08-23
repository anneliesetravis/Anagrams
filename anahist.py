from histogram import histogram
from anagram import make_anagram_dict
from math import log10

words = open("words.txt", "r").readlines()

dictionary = make_anagram_dict(words)

def anagram_count(dictionary):
    """
    Given a dictionary of anagrams, this function counts how many keys have n
    anagrams, for n = 2,...,12, and returns a dictionary where the keys are the
    number of anagrams, and the values are log10 of the number of words in the
    given dictionary with that number of anagrams.

    Arguments:

    :param dictionary: dictionary with keys = alphabetically sorted letters of
    a word and values = anagrams of the key
    
    :return: dictionary with keys = number of anagrams, and values = log10 of the
    number of words with that many anagrams.
    """
    counts = dict()
    
    for n in range(2, 13):
        count = 0
        
        for key in dictionary:
            if len(dictionary[key]) == n:
                count = count + 1
                
        if count != 0:
            counts[n] = log10(count)
        else:
            #cannot calculate log10 of 0, so we substitute with a value of 0
            counts[n] = 0
            
    return counts
            
x = list(anagram_count(dictionary).keys())
y = list(anagram_count(dictionary).values())

print("""Histogram for x = number of anagrams, and y = log10 of the number of words with x number of anagrams""")
histogram(x, y, 30)
