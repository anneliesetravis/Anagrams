import anagram

words = open("words.txt", "r").readlines()

dictionary = anagram.make_anagram_dict(words)

def how_many_anagrams(dictionary):
    """
    Repeatedly asks the user for a word and prints its anagrams (if any) until
    a blank line is inputted - this will end the program.

    Arguments:

    :param dictionary: a dictionary of anagrams
    :print: the number of other anagrams of the word in the dictionary, and
    what these anagrams are (not including the word itself)
    """
    word = input("Enter a word: ")

    #ensuring that the given word has a corresponding key in the given dictionary
    if "".join(sorted(list(word.lower()))) not in dictionary:
    
        print("Word is not in dictionary. Please try another word.")
        word = input("Enter a word: ")

    while word != "":

        #finding the key of the inputted word
        sorted_word = "".join(sorted(list(word.lower())))
        number_of_anagrams = len(dictionary[sorted_word])-1

        anagrams = list(dictionary[sorted_word])
        anagrams.remove(word.lower())
        
        if number_of_anagrams > 1:
            print(word, "has", number_of_anagrams, "other anagrams:", ", ".join(anagrams))

        elif number_of_anagrams == 1:
            print(word, "has", number_of_anagrams, "other anagram:", ", ".join(anagrams))

        else:
            print(word, "has no anagrams")
        
        #repeating the loop 
        word = input("Enter a word: ")
        
        if "".join(sorted(list(word.lower()))) not in dictionary:
            print("Word is not in dictionary. Please try another word.")
            word = input("Enter a word: ")

how_many_anagrams(dictionary)
                        

