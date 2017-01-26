"""
Working with the news and romance genres from the Brown Corpus, find out which days of the week are most newsworthy,
and which are most romantic. Define a variable called  days containing a list of days of the week, 
i.e. ['Monday', ...]. Now tabulate the counts for these words using cfd.tabulate(samples=days). 
Now try the same thing using plot in place of tabulate. You may control the output order of days 
with the help of an extra parameter: samples=['Monday', ...].
"""

import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist(
        (genre, word)
		for genre in ["news", "romance"]
		for word in brown.words(categories=genre))

cfd.tabulate(samples=["Monday", "Friday"])