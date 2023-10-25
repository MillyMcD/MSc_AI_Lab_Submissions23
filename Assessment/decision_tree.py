import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import accuracy_score
from sklearn import tree

class Predictor:
    """
    Predictor class. For training and inferring a decision tree classifier.
    """
    def __init__(self):
        self.__model = DecisionTreeClassifier()
        self.__fitted = False
    
    def train(self,X,y):
        """
        Train the model.

        Parameters
        ----------
        X : `numpy.ndarray`
            The training features
        y : `numpy.ndarray`
            The training labels
        """
        self.__model.fit(X,y)
        self.__fitted = True

    def report_performance(self,X_test,y_test):
        """
        Determine the performance of the trained model using the test data

        Parameters
        ----------
        X : `numpy.ndarray`
            The test features
        y : `numpy.ndarray`
            The test labels
        
        Returns
        -------
        `dict`
            Dict containing accuracy, precision, recall and F1 score
        """
        pred = self.__model.predict(X_test)

        return {'accuracy':accuracy_score(y_test,pred),
                'precision':precision_score(y_test,pred),
                'recall':recall_score(y_test,pred),
                'F1':f1_score(y_test,pred)}
    
    def infer(self,data,return_prob=False):
        """
        Make a prediction for a single sample

        Parameters
        ----------
        data : `numpy.ndarray`
            A single sample of 1 dim
        return_prob : `bool`
            return probabilities

        Returns
        -------

        """
        if not self.__fitted:
            print('Model has not been trained. Please train the model first by calling "train"')
            return
        
        #reshape the data if ndim is only 1
        if data.ndim == 1:
            data = data.reshape(1,-1)
        
        #return probabilities
        if return_prob:
            return self.__model.predict_proba(data)
        
        #else return the class
        else:
            return self.__model.predict(data)
        

        
        
        


    
