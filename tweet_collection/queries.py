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
    hashtags=open(file_path+"/hastag_candidate_"+str(num_candidate)+".txt",'r')
    print(hashtags)
    keywords=open(file_path+"/keywords_candidate_"+str(num_candidate)+".txt",'r')
    return hashtags.readlines()+keywords.readlines()



print(get_candidate_queries(1976143068,'/Users/camille/PycharmProjects/twitterPredictor/CandidateData'))
