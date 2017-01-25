

# Training the Ai to understand my questions or to make actions upon asking

from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier

# stopwords - list of common words that have less meaning
sw = stopwords.words("english")
stemmer = SnowballStemmer("english")
vectorizer = CountVectorizer()


# features = [["play", "music"], ["make", "coffee"], ["open", "door"], ["hello"]]
# labels = [["music"], ["coffee"], ["door"], ["greeting"]]


sentence = ["play music but one of my favorite musical masterpieces"]
stemmed_sentence = ""

for word in sentence[0].split(" "):
    # stemmer - brake down words to "infintive/root" form
    stemmed_sentence += " " + stemmer.stem(word)

list_of_sentences = []
list_of_sentences.append(stemmed_sentence)

# vectorizer - bag of words, words counted by the number of appereance
vectorizer.fit(list_of_sentences)
bag = vectorizer.transform(list_of_sentences)

print bag
