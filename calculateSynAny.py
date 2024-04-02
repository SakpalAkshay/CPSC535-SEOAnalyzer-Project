import nltk
import ssl
from nltk.corpus import wordnet
#try:
 #   _create_unverified_https_context = ssl._create_unverified_context
#except AttributeError:
 #   pass
#else:
 #   ssl._create_default_https_context = _create_unverified_https_context


#nltk.download('wordnet')

# Disable SSL certificate verification


import pandas as pd


def get_synonyms_antonyms(word):
    synonyms = []
    antonyms = []

    # Get synsets (sets of synonyms) for the word
    synsets = wordnet.synsets(word)

    for synset in synsets:
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

    return synonyms, antonyms

def get_synonyms_antonyms_for_df(df):
    # Create empty lists to store synonyms and antonyms
    synonyms_list = []
    antonyms_list = []

    # Iterate through each word in the DataFrame
    for word in df['Word']:
        # Get synonyms and antonyms for the word
        synonyms, antonyms = get_synonyms_antonyms(word)

        # Append synonyms and antonyms to the lists
        synonyms_list.append(synonyms)
        antonyms_list.append(antonyms)

    # Add synonyms and antonyms lists as new columns in the DataFrame
    df['Synonyms'] = synonyms_list
    df['Antonyms'] = antonyms_list

    return df
