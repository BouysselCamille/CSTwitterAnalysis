import os
import tweepy
import json
import tweet_collect.twitter_connection_setup as connect
import pandas as pd
import numpy as np
connexion=connect.twitter_setup()

def collect_to_pandas_dataframe(querry):
    connexion = connect.twitter_setup()
    tweets = connexion.search(querry,language="fr",rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data

data_trump=collect_to_pandas_dataframe("@realDonaldTrump")
data_emmanuel=collect_to_pandas_dataframe("@EmmanuelMacron")
print(data_trump)


# Max RTs:
rt_max  = np.max(data_emmanuel['RTs'])
rt  = data_emmanuel[data_emmanuel.RTs == rt_max].index[0]
print("The tweet with more retweets is: \n{}".format(data_emmanuel['tweet_textual_content'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data_emmanuel['len'][rt]))


#le plus récent
plus_recent=np.max(data_emmanuel['Date'])
rt=data_emmanuel[data_emmanuel.Date == plus_recent].index[0]
print("The most recent tweet is : \n{}".format(data_emmanuel['tweet_textual_content'][rt]))
print("Published {}.\n".format(plus_recent))

#le plus liké
plus_like=np.max(data_emmanuel['Likes'])
rt=data_emmanuel[data_emmanuel.Likes == plus_like].index[0]
print("The most liked tweet is : \n{}".format(data_emmanuel['tweet_textual_content'][rt]))
print("Number of likes: {}.\n".format(plus_like))


#####visualisation####
import matplotlib.pyplot as plt
tfav = pd.Series(data=data_emmanuel['Likes'].values, index=data_emmanuel['Date'])
tret = pd.Series(data=data_emmanuel['RTs'].values, index=data_emmanuel['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()
plt.close()

#Trump vs Macron
tret_macron=pd.Series(data=data_emmanuel['RTs'].values, index=data_emmanuel['Date'])
tret_trump=pd.Series(data=data_trump['RTs'].values, index=data_trump['Date'])

tret_macron.plot(figsize=(16,4), label="Macron", legend=True)
tret_trump.plot(figsize=(16,4), label="Trump", legend=True)

plt.show()
