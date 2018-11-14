import tweet_collect.twitter_connection_setup as connect


def collect(keyword):
    connexion = connect.twitter_setup()
    tweets = connexion.search(keyword,language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)
    return(tweets)
#collect()

def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses
#collect_by_user(1976143068)

import tweepy
from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True




def collect_by_streaming():

    connexion = connect.twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['Emmanuel Macron'])

#collect_by_streaming()


