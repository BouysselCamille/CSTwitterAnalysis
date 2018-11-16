#Libraries
from textblob import TextBlob
from textblob import Word
import textblob
import nltk
import pandas as pd
import numpy as np
from tweet_analysis.sentiment_analysis import collect_to_pandas_dataframe
import matplotlib.pyplot as plt



#Collecting
data_trump,tweets_trump=collect_to_pandas_dataframe("@realDonaldTrump")
data_hilary,tweets_hilary=collect_to_pandas_dataframe("@HillaryClinton")

#Analysing Data

#Graph
tpol_trump = pd.Series(data=data_trump['Sentiment'].values, index=data_trump['Date'])
tpol_hilary = pd.Series(data=data_hilary['Sentiment'].values, index=data_hilary['Date'])
tpol_trump.plot(figsize=(16,4), label="Trump", legend=True)
tpol_hilary.plot(figsize=(16,4), label="Clinton", legend=True)

plt.show()
plt.close()
