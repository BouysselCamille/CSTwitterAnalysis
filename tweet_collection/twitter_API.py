import twitter_collect.twitter_connection_setup as connect
from tweepy.streaming import StreamListener
import tweepy

def collect():
    connexion = connect.twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="french",rpp=100)
    tweet_real = []
    for tweet in tweets:
        if tweet not in tweet_real:
            tweet_real.append(tweet)
            print(tweet.text)

#collect()


def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses

#collect_by_user(25073877)

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


