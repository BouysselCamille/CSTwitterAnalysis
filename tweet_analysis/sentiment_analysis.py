#Libraries
from textblob import TextBlob
from textblob import Word
import textblob
import nltk
import pandas as pd
import numpy as np

#API Connection
import tweet_collect.twitter_connection_setup as connect
connexion=connect.twitter_setup()

#Get Tweets
def collect_to_pandas_dataframe(querry):
    connexion = connect.twitter_setup()
    tweets = connexion.search(querry,language="en",rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    data['Sentiment']= np.array([TextBlob(tweet.text).sentiment.polarity for tweet in tweets])
    return data,tweets
data,tweets=collect_to_pandas_dataframe("@realDonaldTrump")

def tweets_polarity_pos_neu_neg(tweets):
    pos_tweets=[]
    neg_tweets=[]
    neu_tweets=[]
    for tweet in tweets:
        sentiment=TextBlob(tweet.text).sentiment.polarity
        if sentiment >0:
            pos_tweets.append(tweet)
        elif sentiment<0:
            neg_tweets.append(tweet)
        else:
            neu_tweets.append(tweet)
    return pos_tweets,neu_tweets,neg_tweets
pos_tweets,neu_tweets,neg_tweets=tweets_polarity_pos_neu_neg(tweets)
def tweets_polarity(tweets):
    popularity=[]
    for tweet in tweets:
        date=tweet.created_at
        sentiment=TextBlob(tweet.text).sentiment.polarity
        popularity.append((date,sentiment))
    return popularity
#Results
#print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
#print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
#print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))
