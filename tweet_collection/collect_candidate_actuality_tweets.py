import CSTwitterAnalysis.tweet_collection.twitter_API as twitter_API
import CSTwitterAnalysis.twitter_collect.twitter_connection_setup as twitter_connection_setup
from CSTwitterAnalysis.tweet_collection.twitter_API import collect

connexion = twitter_connection_setup.twitter_setup()

""" cette fonction récupère et renvoie les tweets répondant aux requêtes fournies dans la liste queries en se connectant avec les
les accès fourni par le twitter_api"""

def get_tweets_from_candidates_search_queries(queries, twitter_api):
    list_of_tweets = []
    for query in queries:
        list_of_tweets = list_of_tweets + collect(query)
    return list_of_tweets

get_tweets_from_candidates_search_queries(['love','fire'],connexion)
