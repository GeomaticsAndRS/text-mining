text-mining
===========

##Text mining attempts on the corpus of abstracts from cost.eu (COST Actions)##

files ending in _corpus.py populate a collection of scientific abstracts by various means;

in particular cost_corpus.py populates a collection of scientific abstracts from cost.eu.

translate_corpus.R detects the language of the abstracts above (using textcat), and then translates them into English (if needed) using the translateR R package (a Microsoft key is needed to use the Microsoft service).

match.R matches the abstracts from the cost and the other corpora, and ranks the matches using a scalar product of tf_idf vectors, using the R package tm.

filter_score.py prints to screen pairs of documents that have a high matching score.

unicodecsv, selenium and HTMLParser are required Python packages, Firefox is needed to be driven by selenium.
