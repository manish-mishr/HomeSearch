"""
Data Mining Final Project.

Created on 04/13/2016
@author     : Manish Kumar, Prateek Bhat and Ritesh Agarwal
@desc       : Functions to stem words in a sentence and to count the number of same words in two given sentences
@version    : uses Python 2.7
"""

"Import libraries"
from nltk.stem.snowball import SnowballStemmer

"Variable to hold the values of root words of english "
stemmer = SnowballStemmer("english")


"Retuns a string in which each word is stemmed "
def stem(str):
    array = []

    for word in str.lower().split():

        array.append(stemmer.stem(word))

    return " ".join(array)



"Retunrs the count of common words between two strings"
def commonWord(str1, str2):

    count = 0
    for word in str1.split():
        if str2.find(word) >= 0:
            count += 1
    return count


s = stem("dancer")
print s