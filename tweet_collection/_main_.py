import os
import tweepy
from tweet_collection.collect_candidate_actuality_tweets import
def store_tweets(tweets,filename):
    with open(filename, "w") as write_file:
        json.dump(tweets, write_file)


tweets_to_store=
