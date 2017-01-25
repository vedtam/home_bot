import nltk
from nltk import ne_chunk, pos_tag, word_tokenize

#part_of_speech_tagged = pos_tag(word_tokenize(sent))
#result = ne_chunk(part_of_speech_tagged)



sent = "please tell me the time"
tagged = pos_tag(word_tokenize(sent))
chunked = ne_chunk(tagged)

print chunked
#chunked.draw()
