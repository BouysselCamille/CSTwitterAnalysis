import os
import tweepy
import json
import tweet_collect.twitter_connection_setup as connect
import pandas as pd
import numpy as np
connexion=connect.twitter_setup()

def collect_to_pandas_dataframe():
    connexion = connect.twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="fr",rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data

data=collect_to_pandas_dataframe()

print(data)


# Max RTs:
rt_max  = np.max(data['RTs'])
rt  = data[data.RTs == rt_max].index[0]
print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))


#le plus récent
plus_recent=np.max(data['Date'])
rt=data[data.Date == plus_recent].index[0]
print("The most recent tweet is : \n{}".format(data['tweet_textual_content'][rt]))
print("Published {}.\n".format(plus_recent))

#le plus liké
plus_like=np.max(data['Likes'])
rt=data[data.Likes == plus_like].index[0]
print("The most liked tweet is : \n{}".format(data['tweet_textual_content'][rt]))
print("Number of likes: {}.\n".format(plus_like))

import matplotlib.pyplot as plt
tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()
