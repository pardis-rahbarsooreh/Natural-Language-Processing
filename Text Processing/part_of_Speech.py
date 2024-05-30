import nltk
from nltk.corpus import wordnet
from collections import Counter

def get_part_of_speech(word):
    probable_part_of_speech = wordnet.synsets(word)  # synset is a set of all the synonyms of the word

    pos_counts = Counter()
    pos_counts["n"] = len([item for item in probable_part_of_speech if item.pos()=="n"])    # number of synonyms of the word that are nouns
    pos_counts["v"] = len([item for item in probable_part_of_speech if item.pos()=="v"])    # number of synonyms of the word that are verbs
    pos_counts["a"] = len([item for item in probable_part_of_speech if item.pos()=="a"])    # number of synonyms of the word that are adjectives
    pos_counts["r"] = len([item for item in probable_part_of_speech if item.pos()=="r"])    # number of synonyms of the word that are adverbs

    most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
    # in pos_counts.most_common(1)[0][0]: (1) means the one most frequent pos and [0][0] returns only the pos and not the count of pos
    return most_likely_part_of_speech




