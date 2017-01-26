import nltk
from nltk import word_tokenize
from time import gmtime, strftime


# user's question
#sent_tokenized = word_tokenize('please turn on the lights')
# sent_tokenized = word_tokenize('what time is it?')
sent_tokenized = word_tokenize('please play some music')


# open training set
train_sents = []
file = open('command_sentences.txt')
for line in file:
    train_sents.append([nltk.tag.str2tuple(t) for t in line.split()])


# train the tagger and tag the input
unigram_tagger = nltk.UnigramTagger(train_sents)
tagged_sentence = unigram_tagger.tag(sent_tokenized)


# handle intent
def handleIntent(intent):
    if token[0] == "time":
        print "The time is: " + strftime("%H:%M:%S", gmtime())
    elif token[0] == "lights":
        print "The light is turned on"
    elif token[0] == "music":
        print "The music is now playing"
    else:
        print "Sorry, I don't have a function for the intent: " + intent


# check for intents
for token in tagged_sentence:
    # is this token a NOUN?
     if token[1] == "NN":
        handleIntent(token[0])
    # TODO: handle verbs for on/off state
