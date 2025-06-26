# stops words  are  words  or expression that we want to exclude from the text
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
worf_quote = "Sir, I protest. I am not a merry man!"
nltk.download("punk_tab")

words_in_quote=word_tokenize(worf_quote)

stops_words=set(stopwords.words("english"))

filtered_list=[]
for word in words_in_quote:
    if word.casefold() not in stops_words:
        filtered_list.append(word)

# printing the all the 
print("words Quotes:")
print(words_in_quote)
print("stop words")
print(stops_words)
print("Filtered Words:")
print(filtered_list)