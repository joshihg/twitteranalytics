import json
import re
import pandas as pd
import matplotlib.pyplot as plt


tweets_data_path = 'twitter.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print len(tweets_data)

tweets = pd.DataFrame()


tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)


tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')


fig.savefig('lang.png')


tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

fig.savefig('country.png')

#word_in_text(word, text). This function return True if a word is found in text, otherwise it returns False.
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


#Next, we will add 3 columns to our tweets DataFrame.
tweets['india'] = tweets['text'].apply(lambda tweet: word_in_text('india', tweet))
tweets['pakistan'] = tweets['text'].apply(lambda tweet: word_in_text('pakistan', tweet))


#calculate the number of tweets 
print tweets['india'].value_counts()[True]
print tweets['pakistan'].value_counts()[True]



prg_langs = ['india', 'pakistan']
tweets_by_prg_lang = [tweets['india'].value_counts()[True], tweets['pakistan'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: india vs. pakistan ', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()

fig.savefig('comparision.png')

##function that uses regular expressions for retrieving link that start with "http://" or "https://" from a text.

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

#add a column called link to our tweets DataFrame. This column will contain the urls information.
tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

#create a new DataFrame called tweets_relevant_with_link. This DataFrame is a subset of tweets DataFrame and contains all relevant tweets that have a link.

tweets_relevant = tweets[tweets['india'] == True]
tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

#print out all links

print tweets_relevant_with_link[tweets_relevant_with_link['india'] == True]['link']
print tweets_relevant_with_link[tweets_relevant_with_link['pakistan'] == True]['link']

