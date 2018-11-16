from textblob import TextBlob
import nltk
nltk.download()
wiki = TextBlob("Python is a high-level, general-purpose programming language.")
wiki.noun_phrases
