"""
Data Mining Final Project. Product Search Relevance for Home Depot from Kaggle

Created on 04/13/2016
@author     : Manish Kumar, Prateek Bhat and Ritesh Agarwal
@desc       : File has functions which are used by other files
@version    : uses Python 3.4.3
"""

"Import libraries"
import re


''' Global variables '''
Character_list = ['  ',',','$','-','//','..',' / ',' \\ ','.']
Suffix_list = ['er','ing','s','less']


''' Find the Number of common words between two strings'''
def findCommonWord(str1, str2):
    words = str1.split()
    count = 0
    for word in words:
        if str2.find(word)>= 0:
            count += 1
    return count

''' Find the total number of occurence of a given word in a string'''
def countOccurence(word, str, index):
    count = 0
    while index < len(str2):
        index = str.find(word, index)
        if index == -1:
            break
        else:
            count += 1
            index += len(str1)
    return count

''' check whether word is a string or not'''
def checkString(word):
	return isinstance(word,str)


''' Split the words into 2 words if there is fullstop in between and after wards it start with capital Letter'''
def splitWords(word):
	word = re.sub(r"(\w)\.([A-Z])", r"\1 \2", word)	
	word = word.lower()
	return word



'''  Replace the extra characters with a space'''
def replaceCharacters(word):
    for ch in Character_list:
        if ch in word:
            if ch == '//':
				word = word.replace(ch,'/')
            elif ch == '..':
                word = word.replace(ch,' . ')
            elif ch == '.':
                word = word.replace(ch,' . ')
            else:
                word = word.replace(ch, ' ')
    return word

''' Make uniform parameters'''
def uniformParameter(word):
    match = re.search("([0-9]+)( *)\.?",word)
    print "success"
    if None != match:
        RE = 'inches|inch|in|\''
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1in. ", word)
        RE = 'foot|feet|ft|\'\''
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1ft. ", word)
        RE = 'pounds|pound|lbs|lb'
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1lb. ", word)
        RE = '(square|sq) ?\.?(feet|foot|ft)'
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1sq.ft. ", word)
        RE = '(cubic|cu) ?\.?(feet|foot|ft)'
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1cu.ft. ", word)
        RE = 'gallons|gallon|gal'
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1gal. ", word)
        RE = 'ounces|ounce|oz'
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1oz. ", word)
        RE = 'centimeters|cm'
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1cm. ", word)
        RE = 'milimeters|mm'
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1mm. ", word)
        word  = word.replace("°"," degrees ") 
        RE = 'degrees|degree'
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1deg. ", word)
        word = word.replace(" v "," volts ")
        RE = 'volts|volt'
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1volt. ", word)
        RE = 'watts|watt'
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1watt. ", word)
        RE = 'amperes|ampere|amps|amp'
        if re.match(RE,word) is not None:
            word = re.sub(RE,"\1amp. ", word)
    return word



''' Get the root words without suffixes'''
def GetRootWords(str1, str2):
    str2 = str2.lower()
    str2 = re.sub("[^a-z0-9./]"," ", str2)
    str2 = [word for word  in set(str2.split()) if len(word)>2]
    
    words = str1.lower().split(" ")
    finalString = []
    for word in words:
        if len(word)>3:
            newString = []
            newString += GetCharacters(word,str2,True)
            if len(finalString)>1:
                finalString += [word for word in newString if word not in Suffix_list and len(word)>1]
            else:
                finalString.append(word)
        else:
            finalString.append(word)
    return (" ".join(finalString))

def GetCharacters(st, textArray, flag):
    localStr = st
    returnStr = []
    for index in range(len(localStr)):
        for word in textArray:
            if word == s[:-index]:
                returnStr.append(st[:-index])
                st=st[len(st)-index:]
                returnStr += GetCharacters(st, textArray, False)
    if flag:
        index = len(("").join(r))
        if not index ==len(st):
            returnStr.append(st[index:])
    return returnStr


def cleanStr(word): 
    flag = cm.checkString(word)
    
    if flag == True:
        word = cm.splitWords(word)
        word = cm.replaceCharacters(word)
        word = cm.uniformParameter(word)
    else:
        word =  "null"
    return word


