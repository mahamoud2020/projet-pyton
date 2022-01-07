

import os
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import matplotlib.pyplot 
import numpy
import pandas

# mise en place de la matrice X des documents x termes

tVectorizer = CountVectorizer(stop_words=stopwords.words("french") + ['les', 'si', 'ils', 'devant', 'là', 'cette', 'puis', 'cela', 'sans', 'leurs', 'où', 'comme'])
tfVectorizer.fit(book)
X = tfVectorizer.transform(book)
X = X.toarray()
features = tfVectorizer.get_feature_names()
(num_doc, num_f) = X.shape
cloudLabels = features
cloudWeights = numpy.sum(X, axis=0)
dictionary = dict(zip(cloudLabels, cloudWeights))

#  trie par ordre décroissant

sortedValue = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)

print(sortedValue[0:50])

# on s'interesser aux les mots les plus fréquents

freqMots = numpy.where(cloudWeights>50)
X_small = X[:,index]
fSmall = np.array(features)[index]
print(X_small.shape)

(_,num_f_small) = X_small.shape

print(str(num_f_small))

#np.array(index)
numpy.array(features)[index]


# etude sur les cooccurrences

# on s'interesse à  la ressemblance entre les mots

coOccurrence = numpy.matmul(X_small.transpose(), X_small)
idMot = numpy.where(fSmall =="all")[0][0]
scoresCooccu = coOccurrence[idMot,:]
dicoCooccu = dict(zip(fSmall, scoresCooccu))
motsCooccu = sorted(dicoCooccu.items(), key=lambda kv: kv[1], reverse=True)
print(motsCooccu)


sources = []
targets = []
weights = []
for i in range(num_f_small):
    for j in range(num_f_small):
        if ((i != j) & (co_occ[i, j] > 50)):
                sources = sources + [fSmall[i]]
                targets = targets + [fSmall[j]]
                weights = weights + [float(coOccurrence[i, j])]
               


sources = pandas.Series(sources)
targets = pandas.Series(targets)
weights = pandas.Series(weights)


# visualisation 

pandas.concat([sources, targets, weights],axis=1)


# observation sur les collocations

# c-t-d, on observe  les mots qui reviennent ensemble fréquemment 

# importation de la librairie pour manipuler la fonction "word_tokenize"
from nltk.tokenize import word_tokenize
words = [w.lower() for w in word_tokenize(texte)]

# importation de la librairie pour manipuler BigramCollocationFinder
# pour manipuler les bigrammes
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

# mise en place des bigrammes
bigram = BigramCollocationFinder.from_words(words)

#  trie sur les bigrammes selon les pertinences au regarde 

bigram.nbest(BigramAssocMeasures.likelihood_ratio, 30)

from nltk.corpus import stopwords

stop_set = stopwords.words('english')


# cette étape permet d'éliminer les bigrammes avec des mots
# trop petits *ou* qui appartiennent à la liste des mots outils (stopset ici)
filter_stops = lambda w: len(w) < 3 or w in stop_set
bigram.apply_word_filter(filter_stops)

bigram.nbest(BigramAssocMeasures.likelihood_ratio, 30)

# observation sur  les trigrammes , c-t-d suite de trois mots

# comme le bigramme, on doit importer la fonction "TrigramCollocationFinder"

from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

tigram = TrigramCollocationFinder.from_words(words)
tigram.apply_word_filter(filter_stops)
tigram.apply_freq_filter(3)
tigram.nbest(TrigramAssocMeasures.likelihood_ratio, 30)



