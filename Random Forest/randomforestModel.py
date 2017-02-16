"""
Data Mining Final Project. Product Search Relevance for Home Depot from Kaggle

Created on 04/13/2016
@author     : Manish Kumar, Prateek Bhat and Ritesh Agarwal
@desc       : Random Forest to predict the relevance of the search query
@version    : uses Python 3.4.3
"""
"Import libraries"
from sklearn.ensemble import RandomForestRegressor
from sklearn import pipeline, grid_search
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import mean_squared_error, make_scorer
from nltk.stem.porter import *
from common import findCommonWord as com
from collections import defaultdict
import random
random.seed(1024)


class RegressionClass(BaseEstimator, TransformerMixin):
    def fit(self, x, y=None):
        return self
    def transform(self, searchQuery):
        droppedCols=['id','relevance','search_term','product_title','product_description','product_info','attr','brand']
        searchQuery = searchQuery.drop(droppedCols,axis=1).values
        return searchQuery

class textColumn(BaseEstimator, TransformerMixin):
    def __init__(self, key):
        self.key = key
    def fit(self, x, y=None):
        return self
    def transform(self, data):
        return data[self.key].apply(str)


def meanSquaredError(groundTruth, predictions):
    meanError= mean_squared_error(groundTruth, predictions)**0.5
    return meanError

RMSE  = make_scorer(meanSquaredError, greater_is_better=False)

def model(trainX,trainY):
    randomForest = RandomForestRegressor(n_estimators = 500, n_jobs = -1, random_state = 1024, verbose = 1)
    vectorizer = TfidfVectorizer(ngram_range=(1, 1), stop_words='english')
    singularVector = TruncatedSVD(n_components=10, random_state = 1024)
    classifier = pipeline.Pipeline([
            ('union', FeatureUnion(
                        transformer_list = [
                            ('cst',  RegressionClass()),  
                            ('txt1', pipeline.Pipeline([('s1', textColumn(key='search_term')), ('vectorizer1', vectorizer), ('singularVector1', singularVector)])),
                            ('txt2', pipeline.Pipeline([('s2', textColumn(key='product_title')), ('vectorizer2', vectorizer), ('singularVector2', singularVector)])),
                            ('txt3', pipeline.Pipeline([('s3', textColumn(key='product_description')), ('vectorizer3', vectorizer), ('singularVector3', singularVector)])),
                            ('txt4', pipeline.Pipeline([('s4', textColumn(key='brand')), ('vectorizer4', vectorizer), ('singularVector4', singularVector)]))
                            ],
                        transformer_weights = {
                            'cst': 1.0,
                            'txt1': 0.5,
                            'txt2': 0.25,
                            'txt3': 0.0,
                            'txt4': 0.5
                            },
                    #n_jobs = -1
                    )), 
            ('rfr', randomForest)])
    param_grid = {'rfr__max_features': [10], 'rfr__max_depth': [20]}
    model = grid_search.GridSearchCV(estimator = classifier, param_grid = param_grid, n_jobs = -1, cv = 2, verbose = 20, scoring=RMSE)
    model.fit(trainX, trainY)
    return model


