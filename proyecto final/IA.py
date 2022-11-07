from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)

def greeting_response(text):
    text = text.lower()

    bot_greetings = ['hola','buenos dias!','buenas tardes','que tal?','que tal tu dia?']

    user_greetings = ['hola','hi','buenas','hello']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    x = list_var
    for i in range (length):
        for j in (range(length)):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index


def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1],cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0 
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break
    if response_flag == 0:
        bot_response = bot_response+' '+"No te entiendo :V"

    sentence_list.remove(user_input)
    return bot_response


print('MeseroBot: Soy tu mesero personal, ¿En que puedo servirte?')

exit_list = ['adios','bye','salu']

while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('MeseroBot: Adios, ¡vuelva pronto!')
        break
    else:
        if greeting_response(user_input) != None:
            print('MeseroBot: '+greeting_response(user_input))
        else:
            print('MeseroBot: '+bot_response(user_input))
