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
    
    def train(self,X:np.ndarray,y:np.ndarray):
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

    def report_performance(self,X_test:np.ndarray,y_test:np.ndarray):
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

        return {'accuracy':f'{accuracy_score(y_test,pred):.3f}',
                'precision':f'{precision_score(y_test,pred):.3f}',
                'recall':f'{recall_score(y_test,pred):.3f}',
                'f1':f'{f1_score(y_test,pred):.3f}'}
    
    def infer(self,data:np.ndarray,return_prob:bool=False):
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
    
    def is_fitted(self):
        """
        Determine if the model has been fitted.

        Returns
        -------
        `bool`
            if fitted or not
        """
        return self.__fitted

    def get_model(self):
        """"
        Get the model class

        Returns
        -------
        sklearn.tree.DecisionTreeClassifier
        """
        return self.__model

        

        
        
        


    
