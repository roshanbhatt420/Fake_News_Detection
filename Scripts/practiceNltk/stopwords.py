# Stop words are words that you want to ignore, so you filter them out of your text when you’re processing it
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import  word_tokenize

nltk.download("stopwords")
example='Sir, I protest. I am not a merry man!'
print(word_tokenize(example))