import numpy as np
import string
import nltk
import pickle
import os
from nltk.corpus import words
from nltk.corpus import cmudict
from nltk.corpus import words as nltk_words

FILE_NAME = "one_syllable_nouns.pkl"

def create_one_syllable_nouns_list():
    nltk.download('cmudict', quiet=True)
    nltk.download('words', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)

    pronunciations = cmudict.dict()

    def is_noun(word):
        return nltk.pos_tag([word])[0][1].startswith('NN')

    all_words = set(w.lower() for w in nltk_words.words())

    one_syllable_nouns = [word for word in all_words if word in pronunciations 
                          and len(word) <= 7 and is_noun(word)]
    return one_syllable_nouns

def save_list(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_list(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
    
def get_one_syllable_nouns():
    if not os.path.exists(FILE_NAME):
        print("Creating one-syllable nouns list...")
        one_syllable_nouns = create_one_syllable_nouns_list()
        save_list(one_syllable_nouns, FILE_NAME)
        print(f"List saved to {FILE_NAME}")
    else:
        print(f"Loading one-syllable nouns list from {FILE_NAME}")
        one_syllable_nouns = load_list(FILE_NAME)

    return one_syllable_nouns

def generate_memorizable(length, seed=None):
    word_list = get_one_syllable_nouns()
    if seed is not None:
        np.random.seed(seed)

    password = '-'.join(np.random.choice(word_list, length, False))
    return password