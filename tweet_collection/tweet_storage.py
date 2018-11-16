import json
from CSTwitterAnalysis.tweet_collection.twitter_API import collect_by_user

tweets_Donald_Trump = collect_by_user(25073877)

"""fonction qui à partir des tweets status, crée un fichier json contenant le tweet (texte, date au format string,
hashtags, id) repéré par son id"""

def store_tweets(tweets,file_name):
    dico = {}
    for tweet in tweets:
        petit_dico =  {}
        petit_dico['text'] = tweet.text
        date = tweet.created_at
        petit_dico['date'] = str(date)
        petit_dico['hastags'] = tweet.entities['hashtags']
        petit_dico['id'] = tweet.id
        dico[str(tweet.id)] = petit_dico

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(dico, file, indent=4)
    with open(file_name, 'r') as file:
        for line in file:
            print(line)

#store_tweets(tweets_Donald_Trump, 'filename')


