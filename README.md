text-mining
===========

##Text mining attempts on the corpus of abstracts from cost.eu (COST Actions)##

file ending in _corpus.py populate a collection of scientific abstracts by various means;

translate_corpus.py detects the language of the abstracts above (using textcat), and then translates them into English (if needed) using the translateR package (a Microsoft key is needed to use the Microsoft service).

cost_corpus.py populates a collection of scientific abstracts from cost.eu.

match_abstracts.py matches the abstracts from the cost and snf corpora, and ranks the matches using a scalar product of tf_idf vectors, using the package tm.

unicodecsv, selenium and HTMLParser are required Python packages, Firefox is needed to be driven by selenium.
