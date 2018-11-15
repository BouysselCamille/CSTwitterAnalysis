import os
import tweepy

def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    os.chdir(file_path)
    hashtags=open(file_path+"/hashtag_candidate_"+str(num_candidate)+".txt",'r')
    print(hashtags)
    keywords=open(file_path+"/keywords_candidate_"+str(num_candidate)+".txt",'r')
    list_of_querries=hashtags.readlines()+keywords.readlines()
    return [word[:-1] for word in list_of_querries] #on enlève les retours à la ligne



#print(get_candidate_queries(1976143068,'/Users/camille/PycharmProjects/twitterPredictor/CandidateData'))




def get_tweets_from_candidates_search_queries(queries_n, twitter_api):
    """
    récupére et renvoie les tweets répondant aux différentes requêtes.
    :param queries: (list) a list of string queries that can be done to the search API independently
    :param twitter_api: une instance de connexion
    :return: (list) a list of tweets that answer the querries
    """
    print(queries_n)
    tweets=[]
    connexion = connect.twitter_setup()
    for query in queries_n :
        tweets.append(collect(query))
    return tweets

#queries_1976143068=get_candidate_queries(1976143068,'/Users/camille/PycharmProjects/twitterPredictor/CandidateData')
#get_tweets_from_candidates_search_queries(queries_1976143068, connexion)


import tweet_collect.twitter_connection_setup as connect

def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
       print(status.text)
    return statuses
#collect_by_user(1976143068)

def get_replies_to_candidate(num_candidate):
    try :
        total_replies=[]
        connexion = connect.twitter_setup()
        statuses = connexion.user_timeline(id = num_candidate, count = 200)
        for status in statuses:
            id_status=status.id
            replies = connexion.search("Macron" ,in_reply_to_status_id_str=id_status,language="french",rpp=1)
            for reply in replies:
                total_replies.append(reply.text)
                print(reply.text)
        return total_replies
    except tweepy.error.RateLimitError:
        print("Limite de stream de tweet atteinte, revient dans 1h")

#get_replies_to_candidate(1976143068)



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

def stream_tweets_about_candidate(num_candidate):
    connexion = connect.twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    return (stream.filter(track=['Emmanuel Macron']))

tweets=stream_tweets_about_candidate(1976143068)

print(tweets)
