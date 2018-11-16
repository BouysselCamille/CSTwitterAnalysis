import CSTwitterAnalysis.tweet_collection.twitter_API as twitter_API
import CSTwitterAnalysis.twitter_collect.twitter_connection_setup as twitter_connection_setup
import CSTwitterAnalysis.tweet_collection.collect_candidate_actuality_tweets as collect_candidate_actuality_tweets
from CSTwitterAnalysis.tweet_collection.twitter_API import collect_by_user
import tweepy
connexion = twitter_connection_setup.twitter_setup()

"""renvoit pour chaque tweet récent d'un candidat les réponses à ce tweet"""

def get_replies_to_candidate(num_candidate):
    try:
        "On récupère les tweets du candidat"
        connexion = twitter_connection_setup.twitter_setup()
        tweets = collect_by_user(num_candidate)

        "Pour chaque tweet, on cherche les tweets répondant à ce tweet"
        for tweet in tweets:
            print(tweet.text)
            reply_to_tweet = connexion.search('Trump', in_reply_to_id_str = tweet.id_str ,language="french",rpp=10)
            for reply in reply_to_tweet:
                print(reply.text)
                print('\n')

    "Erreur pour si on dépasse la limite de tweets"
    except tweepy.error.RateLimitError:
        print("limite de tweets atteinte")

#get_replies_to_candidate(25073877)


"""récupère les retweets de chaque tweet du candidat, en printant le tweet initial"""

"""def get_retweets_of_candidate(num_candidate):
     try:
        "On récupère les tweets du candidat"
        connexion = twitter_connection_setup.twitter_setup()
        candidate_tweets = collect_by_user(num_candidate)

        "Pour chaque tweet, on cherche ses retweets"
        for tweet in candidate_tweets:
            print(tweet.text)
            print('Les retweets à ce tweet sont :')
            retweet_to_tweet = connexion.search('Trump', in_reply_to_id_str = tweet.id_str, language="french",rpp=10)
            for retweet in retweet_to_tweet:
                if
                print(retweet.text)
                print('\n')
"""

#Je n'arrive pas encore à trouver comment identifier les retweets et à les isoler avec la fonction search
#Je passe à la suite
