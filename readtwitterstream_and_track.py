#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
#access_token = "ENTER YOUR ACCESS TOKEN"
#access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
#consumer_key = "ENTER YOUR API KEY"
#consumer_secret = "ENTER YOUR API SECRET"


#access_token = "ENTER YOUR ACCESS TOKEN"
#access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
#consumer_key = "ENTER YOUR API KEY"
#consumer_secret = "ENTER YOUR API SECRET"



consumer_key = "P0g921yylbkqSoS91XooPRZyX"
consumer_secret = "qoNIRjj0TWj9d9hx7AHdRg4gsoZs0Qozc5fqXbcPGRmAtdeAui"


access_token = "2238895496-s4SiakEfkgjOE6UFcIYGnL9JBpmLzuEgKklQcaF"
access_token_secret = "YKtrTr0lh5NE5MONI3C16dSEnzx2veHfSAUTpKDXePJfP"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['india', 'pakistan'])

