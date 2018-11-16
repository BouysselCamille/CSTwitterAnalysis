#Libraries
from textblob import TextBlob
from textblob import Word
import textblob
import nltk
import pandas as pd
import numpy as np
from tweet_analysis.sentiment_analysis import collect_to_pandas_dataframe
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")

rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
data = data.rolling(7).mean()

sns.lineplot(data=data, palette="tab10", linewidth=2.5)
plt.show()

