#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "818055713708802048-Q8XXIJsuLYrkweTgE8OA4PeBNLedef1"
access_token_secret = "m4XUiZwQ1WkHRpaxnRjcCa8WtOYvHmY1i0TkdxhGLa9HV"
consumer_key = "qlK6g0oHT7JmMThJsouSExV7G"
consumer_secret = "eQ6LVbxV2RoK8REkdVRs3fr54PSueSpyBfppj4hayRReJAnxZ6"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])