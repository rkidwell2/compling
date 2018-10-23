"""
This classifier aims to distinguish between animate and inanimate objects,
giving ratios of what words (and their parts of speech) are most likely to
come before or after them. The most informative features are printed.

"""
from nltk.corpus import brown
from nltk import pos_tag, word_tokenize, classify, NaiveBayesClassifier
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from nltk.classify import apply_features

wn = WordNetLemmatizer()

### create featuresets
def create_featuresets(sents, classes, samples):
    featuresets = []
    for sent in sents:
        for item in sent:
            if item[1][0] == "N":
                word=item[0]
                for label in classes:
                    if wn.lemmatize(word) in samples[label]:
                        featuresets.append((noun_features(sent, sent.index(item)), label))
    return featuresets

def noun_features(sentence, i):
    features = {"POS": sentence[i][1]}
    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-pos"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1][0]
        features["prev-pos"] = sentence[i-1][1]
    if i == len(sentence)-1:
        
        features["next-word"] = "<END>"
        features["next-pos"] = "<END>"
    else:
        features["next-word"] = sentence[i+1][0]
        features["next-pos"] = sentence[i+1][1]
    if i > 1:
        features["preprev-word"] = sentence[i-2][0]
        features["preprev-pos"] = sentence[i-2][1]
    if i < len(sentence)-2:
        features["postnext-word"] = sentence[i+2][0]
        features["postnext-pos"] = sentence[i+2][1]
    if i > 2:
        features["prepreprev-word"] = sentence[i-3][0]
        features["prepreprev-pos"] = sentence[i-3][1]
    if i < len(sentence)-3:
        features["postpostnext-word"] = sentence[i+3][0]
        features["postpostnext-pos"] = sentence[i+3][1] 
    return features   


#Define categories
classes = ['ANIMATE','INANIMATE']
samples = {'ANIMATE': ['he','she','we','they','i','me','you','cat', 'man',
                       'woman', 'boy', 'girl','person','people',],
           'INANIMATE': ['it','box','time', 'space','clock', 'board', 'phone',
                         'history', 'science','car', 'test', 'pen',
                         'computer','stone', 'rock', 'chair','table','brush',
                         'tooth','seat','towel','soap','food','house',
                         ]
           }

sents = brown.tagged_sents()
sents = [[(w[0].lower(),w[1]) for w in sent] for sent in sents]

# Split up data for training and testing
train_sents = sents[:int(len(sents)/2)]
dev_test_sents = sents[-(int(len(sents)/2)):]

# create featuresets for data
train_set = create_featuresets(train_sents, classes, samples)
dev_test_set = create_featuresets(dev_test_sents, classes, samples)

# Train
classifier = NaiveBayesClassifier.train(train_set)

# How accurate the classifier was
accuracy = classify.accuracy(classifier, dev_test_set)

errors = []
for sent in dev_test_sents:
    for item in sent:
        if item[1][0] == "N":
            index = sent.index(item)
            word = item[0]
            for label in classes:
                if wn.lemmatize(word) in samples[label]: 
                    guess = classifier.classify(noun_features(sent, index))
                    if guess != label:
                        errors.append((label, guess, word))



classifier.show_most_informative_features(100)
print('The accuracy of the classifier was: ', accuracy)



