# lets dive into the tagging parts of speech
# it is grammetical term thaht deals with the roles words play when you use them together in sentances 
# in english there are 8 part of speech 
# noun , pronoun , adj, verb, adverb, preposition, Conjunction,, interjection
# implementaion of the tagging and aprts of speech
from nltk.tokenize import word_tokenize
# now actual part of the tagging

import nltk
nltk.download("punk_tab")
nltk.download("averaged_perceptron_tagger_eng")

sagan_quote = """
... If you wish to make an apple pie from scratch,
... you must first invent the universe."""

# tokenizing again
words=word_tokenize(sagan_quote)
print("These are the tokenized words:")
print(words)

words_tagg=nltk.pos_tag(words)
print("word tags")
print(words_tagg)