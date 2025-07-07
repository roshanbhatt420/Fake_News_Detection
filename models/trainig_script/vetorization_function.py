from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer(ngram_range=(1,2), stop_words='english', max_df=0.85, min_df=5)
import pandas as pd

# making function for future  use
def vectorWord(content):
    return vectorizer.fit_transform(content)