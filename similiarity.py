import numpy
from keras.preprocessing.text import text_to_word_sequence
from py_stringmatching.similarity_measure.cosine import Cosine
import pandas as pd

def txt_to_words(text):
    result = text_to_word_sequence(text)
    words = [word for word in result if word.isalpha()]
   # print(words)
    return words

dataset = pd.read_csv("final_dataset.csv")
del dataset['Unnamed: 0']

dataset['hazirlanmasi_sozleri'] = dataset['hazirlanmasi'].apply(lambda x : ([str(elem) for elem in txt_to_words(x)]))
dataset['terkibi_sozleri'] = dataset['terkibi'].apply(lambda x : ([str(elem) for elem in txt_to_words(x)]))
dataset['terkibi_sozler_str'] = dataset['terkibi'].apply(lambda x : ' '.join([str(elem) for elem in txt_to_words(x)]))

cos = Cosine()
def compare_txt(word):
    word = txt_to_words(word)
    lst = list(dataset['terkibi_sozleri'])
    lst_final = []
    lst_final = [cos.get_raw_score(word, item) for item in lst]
    y = max(lst_final)
    if y>0.30:
        return dataset.loc[lst_final.index(y)]['ad'],dataset.loc[lst_final.index(y)]['hazirlanmasi'],dataset.loc[lst_final.index(y)]['img_url']
    else:
        return 'Uyğun yemək tapa bilmədik. Zəhmət olmasa, daha fərqli yazın'

