"""
Data Mining Final Project. Product Search Relevance for Home Depot from Kaggle

Created on 04/13/2016
@author     : Manish Kumar, Prateek Bhat and Ritesh Agarwal
@desc       : Pre-processing of the data
@version    : uses Python 3.4.3
"""
"Import libraries"
requests.packages.urllib3.disable_warnings()
import warnings; warnings.filterwarnings("ignore");
import numpy as np
import pandas as pd
import common as cm
import featureExtractor as ft
from nltk.stem.porter import *

"Stemmer function"
stemmer = PorterStemmer()

def processData(combined):
	combined['search_term'] = combined['search_term'].map(lambda word:cleanStr(word))
	combined['product_title'] = combined['product_title'].map(lambda word:cleanStr(word))
	combined['product_description'] = combined['product_description'].map(lambda word:cleanStr(word))
	combined['brand'] = combined['brand'].map(lambda str:cleanStr(word))



def main(trainLink,testLink, productDescLink):
    trainData, testData, productDesc,brandDesc = RD.readFiles(trainLink, testLink, productDescLink )

    "Length of train data"
    lenTrain = trainData.shape[0]

    "Combine train, test and product description data, so that we can process these files together"
    test_train_combined = pd.concat((trainData, testData), axis=0, ignore_index=True)

    allCombined = pd.merge(test_train_combined, productDesc, how='left', on='product_uid')

    ''' Merging the brand description'''
    allCombined = pd.merge(allCombined, brandDesc, how='left', on='product_uid')

    ''' process data to make it to run for our algorithm '''
    processData(allCombined)

    ''' create features for the processed Data'''
    allCombined = ft.createFeatures(allCombined)




def cleanStr(word): 
	flag = cm.checkString(word)
	
	if flag == True:
		word = cm.splitWords(word)
		word = cm.replaceCharacters(word)
        word = cm.uniformParameter(word)
	else:
		word =  "null"
    return word
    
        



if __name__ == '__main__':

    "Give the address of input files"
    trainLink = "./Data/train.csv"
    testLink = "./Data/test.csv"
    productDescLink = "./Data/product_descriptions.csv"

    main(trainLink,testLink, productDescLink)
