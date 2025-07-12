# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        wordlist: list representation of input_text, where each word is a different element in the list
    """
    wordlist = input_text.split()
    return wordlist


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    word_dict = {}
    for word in input_iterable:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict



### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    letter_frequencies = {}
    for letter in word:
        if letter not in letter_frequencies:
            letter_frequencies[letter] = 1
        else:
            letter_frequencies[letter] += 1
    return letter_frequencies

### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    similarity = 0
    elements = []

    for key in freq_dict1:
        elements.append(key)
        if key in freq_dict2:
            similarity += abs(freq_dict1[key] - freq_dict2[key])
        else:
            similarity += freq_dict1[key]

    for key in freq_dict2:
        if key not in elements:
            elements.append(key)
            similarity += freq_dict2[key]

    similary_score = 1-(similarity/(sum(freq_dict1.values())+sum(freq_dict2.values())))
    return round(similary_score, 2)

    # "Alternate Soln"
    # # Calculate DIFF
    # diff = 0
    # # Check all keys in both dictionaries
    # all_keys = set(freq_dict1.keys()) | set(freq_dict2.keys())
    # for key in all_keys:
    #     if key in freq_dict1 and key in freq_dict2:
    #         diff += abs(freq_dict1[key] - freq_dict2[key])
    #     elif key in freq_dict1:
    #         diff += freq_dict1[key]
    #     else:
    #         diff += freq_dict2[key]
    #
    # # Calculate ALL
    # total = sum(freq_dict1.values()) + sum(freq_dict2.values())
    #
    # # Handle edge case where total is 0 to avoid division by zero
    # if total == 0:
    #     return 1.0
    #
    # # Compute and return the similarity score
    # similarity_score = 1 - (diff / total)
    # return round(similarity_score, 2)

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """

    combined_dict = {}

    all_keys = set(freq_dict1.keys()).union(set(freq_dict2.keys())) #converts keys into set to perform set union & combine unique keys
    for key in all_keys:
        if key in freq_dict1 and key in freq_dict2:
            combined_dict[key] = freq_dict1[key] + freq_dict2[key]
        elif key in freq_dict1:
            combined_dict[key] = freq_dict1[key]
        else:
            combined_dict[key] = freq_dict2[key]
    highest_frequency = max(combined_dict.values())
    most_frequent_words = [key for key, value in combined_dict.items() if value == highest_frequency] #returns all keys with values = highest frequency
    return sorted(most_frequent_words) #alphabetically sorts

### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculated as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """

    #Load file and split into words
    input_text = load_file(file_path) # string
    input_list = text_to_list(input_text) # list of strings/words

    # Compute word frequencies and total words
    word_frequencies = get_frequencies(input_list) # dictionary {word:frequency}
    total_words = len(input_list)  # Total words in document (denominator)

    #calculate TF of each word
    TF = {
        word: count / total_words
        for word, count in word_frequencies.items()
    }

    return TF

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    num_docs = len(file_paths)
    all_words_dict ={} #dict mapping {word: num_docs with word} for all words in all files

    for file_path in file_paths:
        #load files and conv to string
        input_text = load_file(file_path)
        input_list = text_to_list(input_text) #['hello', 'world', 'hello'], ['hello', 'friends']

        # extracts all unique keys in file
        all_keys = {word for word in input_list}  #{'world', 'hello'}, {'hello', 'friends'}

        # add frequency to key once if word appears in file
        for key in all_keys:
            if key in all_words_dict:
                all_words_dict[key] += 1
            else:
                all_words_dict[key] = 1

        #print("all words dict: ", all_words_dict) #Prints {'world': 1, 'hello': 2, 'friends': 1} for dict1 and dict2

    #compute IDF dict: IDF(i) = log_10(total number of documents / number of documents with word *i* in it)

    IDF = {
        word: math.log10(num_docs/count)
        for word, count in sorted(all_words_dict.items())
    }

    return IDF

def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    tf_dict = get_tf(tf_file_path)
    idf_dict = get_idf(idf_file_paths)

    tf_idf_list = [] #initialize list to contain tuples

    for word in tf_dict:
        # Only calculate TF-IDF for words that exist in IDF dictionary
        if word in idf_dict:
            tfidf_score = tf_dict[word] * idf_dict[word]
            tf_idf_list.append((word, tfidf_score))

    tf_idf_list.sort(key=lambda x: (x[1], x[0])) #sorts by score first then alphabetically for same score
    return tf_idf_list


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    # Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    # Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    # Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    # Tests Problem 3: Similarity
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # word1_freq = get_letter_frequencies('toes')
    # word2_freq = get_letter_frequencies('that')
    # word3_freq = get_frequencies('nah')
    # word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    # word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    # word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    # word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1)       # should print 1.0
    # print(word_similarity2)       # should print 0.25
    # print(word_similarity3)       # should print 0.0
    # print(word_similarity4)       # should print 0.4

    # Tests Problem 4: Most Frequent Word(s)
    # freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    # most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    # print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    # tf_text_file = 'tests/student_tests/hello_world.txt'
    # idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    # tf = get_tf(tf_text_file)
    # idf = get_idf(idf_text_files)
    # tf_idf = get_tfidf(tf_text_file, idf_text_files)
    # print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    # print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    # print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]