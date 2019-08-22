#Import the necessary methods from tweepy library

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


import tweepy
import csv

"""
This progream coonnects to twitter and queries tweets based on criteria. 
later dump the tweet in CSV fil

"""


consumer_key = "P0g921yylbkqSoS91XooPRZyX"
consumer_secret = "qoNIRjj0TWj9d9hx7AHdRg4gsoZs0Qozc5fqXbcPGRmAtdeAui"


access_token = "2238895496-s4SiakEfkgjOE6UFcIYGnL9JBpmLzuEgKklQcaF"
access_token_secret = "YKtrTr0lh5NE5MONI3C16dSEnzx2veHfSAUTpKDXePJfP"



#This handles Twitter authetification and the connection to Twitter Streaming API
  
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

    
api = tweepy.API(auth)
# Open/Create a file to append data
csvFile = open('result.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, 
                    q="Modi", 
                    since="2019-08-01", 
                    until="2019-08-16", 
                    lang="en").items():
  csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
  print tweet.created_at, tweet.text
csvFile.close()