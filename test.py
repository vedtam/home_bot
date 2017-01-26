import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.corpus import brown
from nltk.corpus import webtext
from nltk.corpus import nps_chat

#part_of_speech_tagged = pos_tag(word_tokenize(sent))
#result = ne_chunk(part_of_speech_tagged)
#chunked.draw()

sent = 'please turn on the lights'
#sent = 'please turn on the computer'
# sent = "please tell me the time"
tagged = pos_tag(word_tokenize(sent))
# chunked = ne_chunk(tagged)

print tagged

#trained pos tagging

brown_tagged_sents = brown.tagged_sents(categories='news')
#brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print unigram_tagger.tag(word_tokenize(sent))
