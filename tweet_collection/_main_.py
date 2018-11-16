import os
import tweepy
import json
import tweet_collect.twitter_connection_setup as connect
import pandas as pd
import numpy as np
connexion=connect.twitter_setup()


from tweet_collection.collect_candidate_actuality_tweets import get_candidate_queries,get_tweets_from_candidates_search_queries
def store_tweets(tweets,filename):
    os.chdir('/Users/camille/PycharmProjects/twitterPredictor/tweet_collection')
    for tweet in tweets:
        with open(filename, "w") as write_file:
            json.dump(tweet._json, write_file)
    return()

queries_1976143068=get_candidate_queries(1976143068,'/Users/camille/PycharmProjects/twitterPredictor/CandidateData')

tweets_to_store=get_tweets_from_candidates_search_queries(queries_1976143068, connexion)
#print(tweets_to_store)
store_tweets(tweets_to_store,"tweets.json")

from tweet_collect.search import collect
from pytest import *




def collect_to_pandas_dataframe():
    connexion = connect.twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="fr",rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data

data=collect_to_pandas_dataframe()

rt_max  = np.max(data['RTs'])
rt  = data[data.RTs == rt_max].index[0]

# Max RTs:
print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))
