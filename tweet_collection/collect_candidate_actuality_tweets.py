import os

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
    print(os.getcwd())
    print(os.listdir(file_path))
    hashtags=open(file_path+"/hashtag_candidate_"+str(num_candidate)+".txt",'r')
    print(hashtags)
    keywords=open(file_path+"/keywords_candidate_"+str(num_candidate)+".txt",'r')
    list_of_querries=hashtags.readlines()+keywords.readlines()
    return [word[:-1] for word in list_of_querries] #on enlève les retours à la ligne



print(get_candidate_queries(1976143068,'/Users/camille/PycharmProjects/twitterPredictor/CandidateData'))


#from tweet_collect.search import collect
#from tweet_collect.twitter_connection_setup import twitter_setup
connexion = twitter_setup()


def get_tweets_from_candidates_search_queries(queries_n, twitter_api):
    """
    récupére et renvoie les tweets répondant aux différentes requêtes.
    :param queries: (list) a list of string queries that can be done to the search API independently
    :param twitter_api: une instance de connexion
    :return: (list) a list of tweets that answer the querries
    """
    print(queries_n)
    tweets=[]
    for query in queries_n :
        tweets.append(collect(query))
    return tweets

#queries_1976143068=get_candidate_queries(1976143068,'/Users/camille/PycharmProjects/twitterPredictor/CandidateData')
#get_tweets_from_candidates_search_queries(queries_1976143068, connexion)
