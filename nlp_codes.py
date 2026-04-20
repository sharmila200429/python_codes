#NLP codes
#Tokenisation

import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download("punkt_tab")
text="hello hi how are you charan sathwik?"
tokens=word_tokenize(text)
print(tokens)

#stop words
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("punkt_tab")
nltk.download("stopwords")
text="this is a sample code written by abirami"
words=word_tokenize(text)
stop_words=set(stopwords.words("english"))
filtered_words=[word for word in words if word.lower() not in stop_words]  # Fixed: 'woed' -> 'word'
print("original:",text)
print("filtered:"," ".join(filtered_words))

#stemming

from nltk.stem import PorterStemmer  
stemmer=PorterStemmer()              
words=["running","runner","easily","fairly"]
stemmed_words=[stemmer.stem(word)for word in words]
print("stemmed words:",stemmed_words)

#lemmatisation

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download("wordnet")
lemmatizer=WordNetLemmatizer()
Words=["running","runner","easily","fairly"]
lemmatized_words=[lemmatizer.lemmatize(word,pos=wordnet.VERB)for word in Words]  
print("lemmatization_words:",lemmatized_words)

#parts of speech tagging

import nltk
from nltk.tokenize import word_tokenize  
from nltk import pos_tag
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")  
sentence = "The quick brown fox jumps over the lazy dog."
tokens=word_tokenize(sentence)
tagged=pos_tag(tokens)
print(tagged)

#Syntax and parsing
exp = "5+3*3"
result=eval(exp)
print(result)

#Lowercasing
text = "Hello world"
lowercase_text = text.lower()
print(lowercase_text)

#remove special characters
import re
def remove(text):
    return re.sub(r'[^A-Za-z0-9\s]',"",text)
i="hello!@@#$$& World"
c = remove(i)
print(c)            
              
#Remove punctuation

import string
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))  
# Example usage
text = "Hello, world! Let's remove punctuation."
clean_text = remove_punctuation(text)
print(clean_text)

#Bag of words

from sklearn.feature_extraction.text import CountVectorizer
# Sample documents
documents = [
"I love programming in Python",
"Python is great for data science",
"I love learning new programming languages"
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()
print("Feature Names:", feature_names)
print("Bag of Words Model:\n", X.toarray())

#N gram
def n_grams(text, n):
    words = text.split()  
    return [tuple(words[i:i + n]) for i in range(len(words) - n + 1)] 
text = "I love programming in Python"
n = 2
print(n_grams(text, n))
