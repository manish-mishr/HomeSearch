"""
Data Mining Final Project.

Created on 04/13/2016
@author     : Manish Kumar, Prateek Bhat and Ritesh Agarwal
@desc       : Decision tree to predict the relevance of the search query
@version    : uses Python 2.7
"""

"Import Libraries"
from sklearn.tree import DecisionTreeRegressor
from sklearn.cross_validation import KFold
import pandas as pd
import numpy as np

def decisiontree(X_train, Y_train, X_test,id_test ):

    "Applying the method"
    dtr = DecisionTreeRegressor()
    dtr.fit(X_train, Y_train)
    Y_test = dtr.predict(X_test)

    # dtr_scr = dtr.score(X_test, Y_test)
    # print(dtr_scr.mean())

    print "Saving submission\n"
    pd.DataFrame({"id": id_test, "relevance": Y_test}).to_csv('submission.csv', index=False)