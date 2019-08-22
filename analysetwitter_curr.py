# -*- coding: utf-8 -*-
import json
import re
import nltk
import pandas as pd
import matplotlib.pyplot as plt



from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_stop_words(text):
    #print text
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    #print(word_tokens)
    text = filtered_sentence
    print text




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


def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


def remove_emoji(string):
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return(RE_EMOJI.sub(r'', string))
   


def pre_process(mytext): 
    mytext = mytext.lower()
    mytext = re.sub(r'[0-9]+', '', mytext)
    mytext = mytext.strip()
    mytext = remove_emoji(mytext)
    mytext = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', mytext)
    mytext = remove_stop_words(mytext)
    return mytext



for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweet['text'] = pre_process(tweet['text'])
        #print tweet['text']
        tweets_data.append(tweet)
    except:
        continue

#print len(tweets_data)

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)


#print tweets['text']
#tokens = pre_process(tweets['text'])

"""
"""
"""
#Next, we will add 3 columns to our tweets DataFrame.
tweets['india'] = tweets['text'].apply(lambda tweet: word_in_text('india', tweet))
tweets['pakistan'] = tweets['text'].apply(lambda tweet: word_in_text('pakistan', tweet))


#calculate the number of tweets 
print tweets['india'].value_counts()[True]
print tweets['pakistan'].value_counts()[True]

##function that uses regular expressions for retrieving link that start with "http://" or "https://" from a text.

#add a column called link to our tweets DataFrame. This column will contain the urls information.

tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

#create a new DataFrame called tweets_relevant_with_link. This DataFrame is a subset of tweets DataFrame and contains all relevant tweets that have a link.

tweets_relevant = tweets[tweets['india'] == True]
tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

#print out all links

print tweets_relevant_with_link[tweets_relevant_with_link['india'] == True]['link']
print tweets_relevant_with_link[tweets_relevant_with_link['pakistan'] == True]['link']
"""
