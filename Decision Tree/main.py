"""
Data Mining Final Project.

Created on 04/13/2016
@author     : Manish Kumar, Prateek Bhat and Ritesh Agarwal
@desc       :
@version    : uses Python 2.7
"""

"Import libraries"
import numpy as np
import pandas as pd
import requests.packages.urllib3


"Import Modules"
import readData as RD
import StemandCount as SC
# import decisiontree as DT
import spellChecking as SPC
import corrections as CR
# import SVM
# import randomforest as RF

"Disable Insecure Platrofm warnings"
requests.packages.urllib3.disable_warnings()

def processData(combinedData):
    combinedData['search_term'] = combinedData['search_term'].map(lambda x: SC.stem(x))

    combinedData['product_title'] = combinedData['product_title'].map(lambda x: SC.stem(x))

    combinedData['product_description'] = combinedData['product_description'].map(lambda x: SC.stem(x))

    print "Done with processing data\n"

    return combinedData

"Function to create new features from current data"
def createnewFearures(combinedData):

    "A new feature representing the length of the search query"
    combinedData['len_of_query'] = combinedData['search_term'].map(lambda x: len(x.split())).astype(np.int64)

    "Combine search_term, product_title and product_description in one single feature"
    combinedData['product_info'] = combinedData['search_term'] + "\t" + combinedData['product_title'] + "\t" + combinedData['product_description']

    "New feature giving the common words between search_term and product_tilte"
    combinedData['word_in_title'] = combinedData['product_info'].map(lambda x: SC.commonWord(x.split('\t')[0], x.split('\t')[1]))

    "New feature giving the common words between search_term and product_description"
    combinedData['word_in_description'] = combinedData['product_info'].map(lambda x: SC.commonWord(x.split('\t')[0], x.split('\t')[2]))

    print "Done with creating new features\n"

    return combinedData

def main(trainLink,testLink, productDescLink):
    trainData, testData, productDesc = RD.readFiles(trainLink, testLink, productDescLink )

    "Length of train data"
    lenTrain = trainData.shape[0]

    "Combine train, test and product description data, so that we can process these files together"
    test_train_combined = pd.concat((trainData, testData), axis=0, ignore_index=True)
    # print test_train_combined.head()
    # print "\n"
    # raw_input()
    allCombined = pd.merge(test_train_combined, productDesc, how='left', on='product_uid')
    # print allCombined.head()
    # raw_input()

    # print "Before processing = ", allCombined.head()


    "Rectify spelling mistakes"
    print "Begin spell check\n"
    # allCombined.to_csv("allCombined.csv")
    # allCombined['search_term'] = allCombined['search_term'].map(lambda x: SPC.spellCheck(x))
    allCombined['search_term'] = allCombined['search_term'].map(lambda x: CR.correct(x))
    print "End spell check\n"

    "Process data"
    allCombined = processData(allCombined)

    "Make new features"
    allCombined = createnewFearures(allCombined)

    """Drop columns 'search_term','product_title','product_description','product_info'
    to preapare train and test data for decision tree to train"""
    allCombined = allCombined.drop(['search_term','product_title','product_description','product_info'],axis=1)


    train = allCombined.iloc[:lenTrain]
    test = allCombined.iloc[lenTrain:]
    id_test = test['id']

    "Prepare data to train Decision tree"
    X_train = train.drop(['id', 'relevance'], axis=1).values
    Y_train = train['relevance'].values


    "Data to predict on"
    X_test = test.drop(['id','relevance'],axis=1).values

    # DT.decisiontree(X_train,Y_train,X_test,id_test)
    # SVM.svm(X_train,Y_train,X_test,id_test)
    RF.randForest(X_train,Y_train,X_test,id_test)


if __name__ == '__main__':

    "Give the address of input files"
    trainLink = "Data/train.csv"
    testLink = "Data/test.csv"
    productDescLink = "Data/product_descriptions.csv"

    main(trainLink,testLink, productDescLink)