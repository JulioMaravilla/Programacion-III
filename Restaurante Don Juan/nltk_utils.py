import numpy as np
import nltk

# nltk.download('punkt') # Es un conjunto de bibliotecas y programas para el procesamiento del lenguaje natural
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
#tokenizar la oracion
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

#derivamos para encontrar la raiz de cada palabra y las pasamos a minisculas
def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    # derivamos cada palabra
    sentence_words = [stem(word) for word in tokenized_sentence]
    #inicializamos la bolsa con 0 para cada palabra
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag