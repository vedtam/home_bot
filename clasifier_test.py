import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.corpus import brown
from time import gmtime, strftime


# name last letter clasifier

def gender_features(word):
    return {'last_letter': word[-1]}


from nltk.corpus import names

# returns like: ({'last_letter': 'o'}, 'male'), ({'last_letter': 'r'}, 'male') ...
labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])

import random
random.shuffle(labeled_names)


featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)


print classifier.classify(gender_features('Victoria'))
print(nltk.classify.accuracy(classifier, test_set))


# Dialog act classifier

# posts = nltk.corpus.nps_chat.xml_posts()[:10]
#
# def dialogue_act_features(post):
#     features = {}
#     for word in nltk.word_tokenize(post):
#         features['contains({})'.format(word.lower())] = True
#         return features
#
# # featuresets returns: [({'contains(now)': True}, 'Statement'), ({'contains(hey)': True}, 'Greet'), ... ]
# featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
# size = int(len(featuresets) * 0.1)
#
# train_set, test_set = featuresets[size:], featuresets[:size]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
#
# #print(nltk.classify.accuracy(classifier, test_set))
