"""
Data Mining Final Project.

Created on 04/13/2016
@author     : Manish Kumar, Prateek Bhat and Ritesh Agarwal
@desc       : Define the environment for Kuhn Poker
@version    : uses Python 2.7
"""

"Import libraries"
import numpy as np
import pandas as pd



def readFiles(trainlink, testlink, productlink):
    trainData = pd.read_csv("Data/train.csv",encoding="ISO-8859-1")

    testData = pd.read_csv("Data/test.csv",encoding="ISO-8859-1")
    # print testData.head()
    # raw_input()
    productDesc = pd.read_csv("Data/product_descriptions.csv")
    return trainData, testData, productDesc

# trainLink = "Data/train.csv"
# testLink = "Data/test.csv"
# productDescLink = "Data/product_descriptions.csv"
#
# readFiles(trainLink, testLink, productDescLink )