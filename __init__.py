import nltk
from nltk.corpus import treebank
from nltk.corpus import wordnet as wn

#sentence = """At eight o'clock on Thursday morning... Arthur didn't feel very good."""
#tokens = nltk.word_tokenize(sentence)
#print tokens

#tagged = nltk.pos_tag(tokens)
#print tagged[0:6]

syno_set = wn.synsets('good')  # @UndefinedVariable
print syno_set

a = 1