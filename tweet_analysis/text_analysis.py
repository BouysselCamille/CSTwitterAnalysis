from textblob import TextBlob
from textblob import Word
import nltk

import tweet_collect.twitter_connection_setup as connect
connexion=connect.twitter_setup()

tweets = connexion.search("@realDonaldTrump",language="english",rpp=1)
list_of_text_to_lemmatize=[]
for tweet in tweets :
    words=TextBlob(tweet.text).words
    for word in words:
        if word not in list_of_text_to_lemmatize:
            list_of_text_to_lemmatize.append(word)



list_of_word_lemmatized=[]
list_of_forgiden_caracters=["…",'/','’','‘',"_","1","2","3","4","5","6","7","8","9","'","😘",'”','“','http','😂']

for word in list_of_text_to_lemmatize:
    word=word.lower()
    for carac in list_of_forgiden_caracters:
        if carac in word:
            continue
    if len(word)>=3 and Word(word).detect_language()!='en':
        continue
    if TextBlob(word).tags[0][1][0]=='V':
        word_lemmatized=Word(word).lemmatize("v")
    else:
        word_lemmatized=Word(word).lemmatize()

    if word_lemmatized not in list_of_word_lemmatized:
        list_of_word_lemmatized.append(word_lemmatized)

print(list_of_word_lemmatized)
