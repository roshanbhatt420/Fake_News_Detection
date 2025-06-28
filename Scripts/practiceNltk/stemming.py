# stemmming =text preprocessing task in whihc we reduce the word in their base or root word like dicovering to deicover 
# implementing the stemming 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
nltk.download("punk_tab")
stemmer=PorterStemmer()
string_to_be_stemming="""The crew of the USS Discovery discovered many discoveries. Discovering is what explorers do."""
# before stemming the all word we have to tokenize the words 
words=word_tokenize(string_to_be_stemming)
print("Word tokenized")
print(words)
# creating the stemming words
stemmed_words=[stemmer.stem(word) for word in words]
print("Stemmed words are:")
print(stemmed_words)
