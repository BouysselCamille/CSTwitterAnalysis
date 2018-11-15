import os
import tweepy
import json
import tweet_collect.twitter_connection_setup as connect
connexion=connect.twitter_setup()


from tweet_collection.collect_candidate_actuality_tweets import get_candidate_queries,get_tweets_from_candidates_search_queries
def store_tweets(tweets,filename):
    for tweet in tweets[1]:
        print(tweet)
        with open(filename, "w") as write_file:
            json.dump(tweet, write_file)
    return()

queries_1976143068=get_candidate_queries(1976143068,'/Users/camille/PycharmProjects/twitterPredictor/CandidateData')

tweets_to_store=get_tweets_from_candidates_search_queries(queries_1976143068, connexion)
print(tweets_to_store)
store_tweets(tweets_to_store,"tweets.json")


