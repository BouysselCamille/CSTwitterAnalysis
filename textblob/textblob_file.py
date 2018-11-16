from textblob import *
import CSTwitterAnalysis.twitter_collect.twitter_connection_setup as connect
from tweepy.streaming import StreamListener
import tweepy
from CSTwitterAnalysis.tweet_collection.twitter_API import collect



"""fonction qui extrait le vocabulaire d'un tweet"""

def extract_word_from_tweet(tweet):
    text = TextBlob(tweet.text)
    #for word in text.words:
        #print(word)
    return text.words

#print(extract_word_from_tweet(tweet))


"""fonction qui extrait les phrases d'un tweet"""

def extract_sentence_from_tweet(tweet):
    text = TextBlob(tweet.text)
    #for word in text.words:
        #print(word)
    return text.sentences

#print(extract_sentence_from_tweet(tweet))

"""fonction qui extrait le sentiment général d'un tweet"""

def extract_sentiment_from_tweet(tweet):
    text = TextBlob(tweet.text)
    return text.sentiment

"""fonction qui corrige un texte"""

def correct_text(tweet):
    text = TextBlob(tweet.text)
    #print(text.correct())
    return text.correct()
