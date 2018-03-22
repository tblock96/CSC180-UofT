'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.

Modified to fit the requirements of CSC180 Project 3 by Theodore Block.
Last modified: Nov. 28, 2016.
'''

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in list(vec.values()):
        sum_of_squares += x**2
    return sum_of_squares**0.5


def cosine_similarity(vec1, vec2):
    new_dict = {}
    for key in list(vec1.keys()):
        if key in list(vec2.keys()):
            new_dict[key] = vec1[key]*vec2[key]
    sum, mag1, mag2 = 0, 0, 0
    for value in list(new_dict.values()):
        sum += value
    for value in list(vec1.values()):
        mag1 += value**2
    for value in list(vec2.values()):
        mag2 += value**2
    mag = (mag1*mag2)**0.5
    return sum/mag

def get_other_words(word, sentence):
    '''Return a dictionary of the number of times each other word appears in the
    sentence
    
    word - the given word
    sentence - a list of words'''
    d = {}
    for w in sentence:
        if w == word:
            continue
        elif w not in list(d.keys()):
            d[w] = 1
        else:
            d[w] += 1
    return d

def get_descriptors(sentence):
    '''Return a dictionary of all the words in the sentence, with each value
    being a dictionary -- the result of get_other_words
    
    sentence - a list of words'''
    d = {}
    for w in sentence:
        if w not in list(d.keys()):
            d[w] = get_other_words(w, sentence)
    return d

def build_semantic_descriptors(sentences):
    '''Return a dictionary that combines all dictionaries from each sentence
    
    sentences - a list of lists of words'''
    dictionaries = []
    big_dictionary = {}
    for s in sentences:
        dictionaries.append(get_descriptors(s))
    for sentence in dictionaries:
        for word in list(sentence.keys()):
            if word not in big_dictionary:
                big_dictionary[word] = sentence[word]
            else:
                for w in list(sentence[word]):
                    if w not in big_dictionary[word]:
                        big_dictionary[word][w] = sentence[word][w]
                    else:
                        big_dictionary[word][w] += sentence[word][w]
    return big_dictionary

def build_semantic_descriptors_from_files(filenames):
    return build_semantic_descriptors(get_mult_texts(filenames))

def build_semantic_descriptors_from_partial_files(filenames, tenth):
    return build_semantic_descriptors(get_mult_part_texts(filenames, tenth))

def get_text(filename):
    text = open(filename, encoding="latin1").read().lower()
    text = text.replace(",", "").replace("-", "").replace("--", "")\
    .replace(":", "").replace(";", "").replace("!", ".").replace("?", ".")
    split = text.split(".")
    for i in range(len(split)):
        split[i] = split[i].split()
    return split

def get_partial_text(filename, tenth):
    '''Return a list of sentences, each formatted as a list of words, from
    the given amount of the file filename
    
    Args:
    filename: the file to be parsed
    tenth: the number of tenths to be used of the text from filename
    '''
    text = open(filename, encoding='latin1').read()
    text = text[:(len(text)*tenth)//10]
    text = text.lower().replace(",", "").replace("-", "").replace("--", "")\
    .replace(":", "").replace(";", "").replace("!", ".").replace("?", ".")
    split = text.split(".")
    for i in range(len(split)):
        split[i] = split[i].split()
    return split

def get_mult_texts(filenames):
    big_list = []
    for file in filenames:
        for list in get_text(file)[:]:
            big_list.append(list[:])
    return big_list
    
def get_mult_part_texts(filenames, tenth):
    big_list = []
    for file in filenames:
        for list in get_partial_text(file, tenth)[:]:
            big_list.append(list[:])
    return big_list

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    '''Return the element of choices which scores most highly in similarity
    to word based on similarity_fn and semantic_descriptors'''
    max_sim = -100000
    max_choice = ""
    for choice in choices:
        try:
            sim = similarity_fn(semantic_descriptors[word],\
            semantic_descriptors[choice])
        except KeyError:
            sim = -1
        if sim > max_sim:
            max_sim, max_choice = sim, choice
    return max_choice

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    tests = get_tests(filename)
    count_pass = 0
    for test in tests:
        if most_similar_word(test[0], test[2:],\
        semantic_descriptors, similarity_fn) == test[1]:
            count_pass += 1
    return 100*count_pass/len(tests)

def get_tests(filename):
    '''Return a list of lists that have the test format from a testing
    file with the name filename
    '''
    
    f = open(filename, encoding="latin1").read().split("\n")
    tests = []
    for line in f:
        tests.append(line.split())
    return tests

def add_dicts(vec1, vec2):
    new_dict = {}
    for word in list(vec1.keys()):
        new_dict[word] = vec1[word]
    for word in list(vec2.keys()):
        if word not in list(new_dict.keys()):
            new_dict[word] = vec2[word]
        else:
            new_dict[word] += vec2[word]
    return new_dict

def get_negative_vector(vec):
    new_vec = {}
    for key in list(vec.keys()):
        new_vec[key] = -vec[key]
    return new_vec
    
def sim_euc(vec1, vec2):
    return -norm(add_dicts(vec1, get_negative_vector(vec2)))

def sim_euc_norm(vec1, vec2):
    norm_v1, norm_v2 = norm(vec1), norm(vec2)
    new_v1, new_v2 = {}, {}
    for i in range(2):
        vec = [vec1, vec2][i]
        for word in list(vec.keys()):
            [new_v1, new_v2][i][word] = vec[word] / [norm_v1, norm_v2][i]
    return sim_euc(new_v1, new_v2)