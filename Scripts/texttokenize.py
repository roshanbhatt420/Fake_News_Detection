from nltk.tokenize import sent_tokenize,word_tokenize
import nltk
nltk.download('punkt_tab')
# you can conveniently split up text by word or by sentence.
# types of  tokenize is 
# tokenize by word and tokenize by sentence

exmaple_text="""When you tokenize by sentence, you can analyze how those words relate to one another and see more context. Are there a lot of negative words around the word “Python” because the hiring manager doesn’t like Python? Are there more terms from the domain of herpetology than the domain of software development, suggesting that you may be dealing with an entirely different kind of python than you were expecting?"""
print(sent_tokenize(exmaple_text))
print(word_tokenize(exmaple_text))