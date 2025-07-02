# Importing necessary libraries
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data (only once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Function for preprocessing
def Preprocessing_module(title, text):
    # Convert to lowercase
    title = title.lower()
    text = text.lower()

    # Combine title and text
    combined_text = title + " " + text

    # Tokenize the combined text
    tokens = word_tokenize(combined_text)

    # Remove punctuation
    tokens = [word for word in tokens if word not in string.punctuation]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens

# Sample input
title = "This is the title of the reading and studying the most wanted ball BLock"
text = "My name is Roshan Bhatta and you know who I am"

# Run preprocessing
processed_tokens = Preprocessing_module(title, text)

# Output
print("Processed Tokens:\n", processed_tokens)
