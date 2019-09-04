

import json
import re
import nltk
import string
from unicodedata import normalize
import pandas as pd
from collections import Counter
import matplotlib.pyplot as pl


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    my_stop_words = ['\'\'','``','rt@','https','http','...','\u2060','\206','$',"n't",'RT','from','rom','&amp;','rt',',','#','\'s','\n','http\/\/','https\/\/','.','!','...','%','&','https//','http//','\'','','`','\'re','-','"','\"']
    word_tokens = word_tokenize(text)
    #print word_tokens
    filtered_sentence = []
    for w in word_tokens:
        w = str(w)
        if w not in stop_words:
            if w not in my_stop_words:
                    filtered_sentence.append(w)
    text = filtered_sentence
    #print text
    return text
    

tweets_data_path = 'twitterdata.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")

tweets = pd.DataFrame()

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


def remove_emoji(string):
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return(RE_EMOJI.sub(r'', string))

 
def remove_punc(text):
    text = text.translate(string.maketrans("",""), string.punctuation)
    return text


def pre_process(mytext): 
    #print mytext
    # Wokring. Ignoring who tweeted
    mytext = re.sub(r'http.*$',"",mytext)
    ## wokring below but it is replacing all so not sure. It is not ignoring who tweeted
    #mytext = re.sub(r':.*$', ":", mytext)
    mytext = mytext.lower()
    #mytext = re.sub(r'[0-9]+','', mytext)
    #print mytext
    mytext = mytext.strip()
    #print mytext
    mytext = remove_emoji(mytext)
    mytext = re.sub('@[^\s]+','',mytext)
    #print my_text
    mytext = remove_stop_words(mytext)
    return mytext


for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweet['text'] = pre_process(tweet['text'])
        tweets_data.append(tweet)
    except:
        continue

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

print tweets['text']

full_list = []  # list containing all words of all texts
for elmnt in tweets['text']:  # loop over lists in df
    full_list += elmnt  # append elements of lists to full list
    #print elmnt

#print full_list

val_counts = pd.Series(full_list).value_counts()  # make temporary Series to count

print val_counts[:20]



#