#Libraries
from textblob import TextBlob
from textblob import Word
import textblob
import nltk
import pandas as pd
import numpy as np
from tweet_analysis.sentiment_analysis import collect_to_pandas_dataframe
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid")
#Import Data
data,tweets=collect_to_pandas_dataframe("@realDonaldTrump")
dates=data['Date']
values=data['Sentiment']
data = pd.DataFrame(values, dates, columns=["Trump"])


sns.lineplot(data=data, palette="tab10", linewidth=2.5)
plt.show()

