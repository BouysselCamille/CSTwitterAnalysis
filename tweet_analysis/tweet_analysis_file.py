from pandas import *
import numpy as np


def max_retweet(data):
    rt_max = np.max(data['RTs'])
    rt = data[data.RTs == rt_max].index[0]

    # Max RTs:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))

def max_likes(data):
    likes_max = np.max(data['Likes'])
    tweet = data[data.Likes == likes_max].index[0]

    # Max likes:
    print("The tweet with more likes is: \n{}".format(data['tweet_textual_content'][tweet]))
    print("Number of likes: {}".format(likes_max))
    print("{} characters.\n".format(data['len'][tweet]))


def tweet_with_length(data,length):
    index_tweets = [data[data.len == length].index[0]]
    print("The tweets whose lenght is {} are :\n{}".format(str(length),data['tweet_textual_content'][tweet]) for tweet in index_tweets)

def nombre_tweets_retweetes_plus_de_n_fois(data,n):
    index_tweets = data[data.RTs >= n].index[0]
    compteur = 0
    for index in index_tweets:
        print(data['tweet_textual_content'][index]+', number of retweets: {}'.format(data.RTs[index]))
        compteur += 1
    return compteur
