import textblob
from textblob import TextBlob
import CSTwitterAnalysis.twitter_collect.twitter_connection_setup as connect
from tweepy.streaming import StreamListener
import tweepy
from nltk.corpus import stopwords
from CSTwitterAnalysis.tweet_collection.twitter_API import collect_un_tweet
import nltk
nltk.download('stopwords')


tweet = collect_un_tweet('Trump')
print(tweet.text)
#print("ok")


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
    #for word in text.sentence:
        #print(sentence)
    return text.sentences

#print(extract_sentence_from_tweet(tweet))

"""fonction qui extrait le sentiment général d'un tweet"""

def extract_sentiment_from_tweet(tweet):
    text = TextBlob(tweet.text)
    print(text)
    return text.sentiment

#print(extract_sentiment_from_tweet(tweet))

"""fonction qui corrige un texte"""

def correct_text(tweet):
    text = TextBlob(tweet.text)
    #print(text.correct())
    return text.correct()


"""fonction qui supprime les mots interdits du tweet """

def supprime_mots_interdits(tweet):
    words = extract_word_from_tweet(tweet)
    mots_interdits = []
    new_tweet_words = []
    for word in words:
        #print ('ok')
        if word not in mots_interdits:
            new_tweet_words.append(word)
        else:
            new_tweet_words.append('***')
    #new_tweet_words.join(' ')
    return new_tweet_words

#print(supprime_mots_interdits(tweet))

def supprime_mots_trop_communs(tweet):
    words = extract_word_from_tweet(tweet)
    stop_words = set(stopwords.words('english'))
    new_words = []
    for word in words:
        if word not in stop_words:
            new_words.append(word)
    return new_words

print(supprime_mots_trop_communs(tweet))
