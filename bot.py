import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.corpus import brown
from time import gmtime, strftime

sent_tokenized = word_tokenize('What time it is?')

train_sents = []
file = open('document.txt')
for line in file:
    train_sents.append([nltk.tag.str2tuple(t) for t in line.split()])


unigram_tagger = nltk.UnigramTagger(train_sents)
tagged_sentence = unigram_tagger.tag(sent_tokenized)

for token in tagged_sentence:
    if token[0] == "time" and token[1] == "NN":
        print "The time is: " + strftime("%H:%M:%S", gmtime())
