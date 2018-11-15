import CSTwitterAnalysis.tweet_collection.twitter_API as api
import os

"""Cette fonction permet de créer une liste de mots qu'on utilisera dans les searchs à partir du numéro du candidat et de 2 dossiers
contenant des mots-clé et des hashtag.
On se rend dans le bon fichier grâce à un chemin relatif puis on ouvre les fichiers, on liste les mots avec readlines()
et on les reliste en supprimant /n"""

def get_candidate_queries(num_candidate, file_path):
    with open(file_path+'hashtag_candidate_'+str(num_candidate)+".txt", 'r') as file_hashtag:
        list_of_hashtag = file_hashtag.readlines()
    with open(file_path+'keyword_candidate_'+str(num_candidate)+".txt", 'r') as file_keyword:
        list_of_keyword = file_keyword.readlines()
    return ([hashtag[:-1] for hashtag in list_of_hashtag] + [keyword[:-1] for keyword in list_of_keyword])

print (get_candidate_queries(1,'../CandidateData/'))



"""Première fonction test"""
def fonction2(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtagfiles
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    """ on ouvre les deux fichiers et on conserve chaque mot-clé ou hashtag dans une liste sous forme de chaîne de caractères"""
    hashtags = open(file_path+str(num_candidate)+".txt","r")
    list_of_hashtags = hashtags.readlines()
    return [word[:-1] for word in list_of_hashtags]

print(fonction2(1,"../CandidateData/hashtag_candidate_"))
