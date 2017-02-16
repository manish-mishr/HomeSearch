"""
Data Mining Final Project. Product Search Relevance for Home Depot from Kaggle

Created on 04/13/2016
@author     : Manish Kumar, Prateek Bhat and Ritesh Agarwal
@desc       : Takes the input data and calls the model to predict the output
@version    : uses Python 3.4.3
"""

"Import libraries"
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, make_scorer
from nltk.stem.porter import *
stemmer = PorterStemmer()
from collections import defaultdict
import random
from sklearn.feature_extraction import text
import nltk

"Import modules"
import randomforestModel as rm 
from common import findCommonWord as com

random.seed(1024)


def prepareData(datalink,length):
    allData = pd.read_csv("processed.csv",encoding="ISO-8859-1")
    trainData = allData.iloc[:length]
    testData = allData.iloc[length:]
    testID = testData['id']
    trainY = trainData['relevance'].values
    trainX =trainData[:]
    testX = testData[:]
    return trainY,trainX,testX


def prediction(trainY,trainX,testX,testID):
    model = rm.model(trainX,trainY)
    predictY = model.predict(X_test)
    pd.DataFrame({"id": testID, "relevance": predictY}).to_csv('Kaggle_submission.csv',index=False)

    trainingData = pd.read_csv('processed.csv', encoding="ISO-8859-1", index_col=0)

    stopWords = []
    dataDict= defaultdict()

    for index in range(len(trainingData)):
        searchTerm = str(trainingData['search_term'][index]).lower()

        allWords = set(searchTerm.split(" "))
        for word in allWords:
		if word not in stopWords and len(word)>0:
	                if word not in trainingData:
				try:
					trainingData[word] = [1,com(word, trainingData['product_title'][index]),com(word, trainingData['brand'][index]),com(word, trainingData['product_description'][index])]
				except:
					continue
		        else:
		            trainingData[word][0] += 1
		            trainingData[word][1] += com(word, trainingData['product_title'][index])
		            trainingData[word][2] += com(word, trainingData['brand'][index])
		            trainingData[word][3] += com(wod, trainingData['product_description'][index])

	    newDataDict = pd.DataFrame.from_dict(trainingData,orient='index')
	    newDataDict.columns = ['count','in title','in brand','in prod']
	    newDataDict = newDataDict.sort_values(by=['count'], ascending=[False])

	    filename = open("Finalreview.csv", "w")
	    filename.write("word|count|in title|in brand|in description\n")
	    for ind in range(len(newDataDict)):
		filename.write(newDataDict.index[ind] + "|" + str(newDataDict["count"][ind]) + "|" + str(newDataDict["in title"][ind]) + "|" + str(newDataDict["in brand"][ind]) + "|" + str(newDataDict["in prod"][ind]) + "\n")
	    filename.close()


if __name__ == '__main__':
   trainY,trainX,testX,testID = prepareData("./processed.csv",74067)
   prediction()
