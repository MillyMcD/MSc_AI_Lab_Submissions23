import numpy as np
from database_client import DatabaseClient
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataLoader:
    """
    DataLoader class. Loads the data, cleans it, and prepares it for training.
    Also provides a method for cleaning inference samples

    Parameters
    ----------
    client : `DatabaseClient`
        The database client
    collection : `str`
        Name of the collection
    """
    def __init__(self,client:DatabaseClient,collection:str):
        self.__dbclient = client

        #make sure client is available, then get all records
        if self.__dbclient.is_logged_in():
            self.__raw_data = self.__dbclient.get_all_records(collection,True)
        else:
            print('Client not available. Check credentials')
    
    def clean_data(self):
        """
        Clean the data. Drop NaN rows and drop duplicates. This dataset is already 
        relatively clean. Could add log scaling to reduce skewness...
        """
        #drop any rows with NaN values
        dataset = self.__raw_data.dropna()

        #drop any duplicates
        dataset = dataset.drop_duplicates()

        return dataset

    def prepare_data_training(self,clean:bool=True,test_size:float=0.2):
        """
        Prepare the training data

        Parameters
        ----------
        clean : `bool`
            Clean the data
        test_size : `float`
            Size of the test dataset

        Returns
        -------
        tuple
            train features, test features, train labels and test labels
        """
        #clean the data or not
        if clean:
            data = self.clean_data()
        else:
            data = self.__raw_data.copy()

        #grab feature columns and class column
        label_column = 'Class'
        feat_column  = [i for i in list(data.columns) if label_column != i]

        #split data into feature and labels
        X = data[feat_column].values
        y = data[label_column].values

        #split data into train/test in stratified way so label balance is same in train/test
        X_train, X_test, y_train, y_test = train_test_split(X,y,stratify=y,test_size=test_size)
        
        #create normalisation scaler
        self.__scaler = StandardScaler()
        self.__scaler.fit(X_train)
        X_train = self.__scaler.transform(X_train)
        X_test  = self.__scaler.transform(X_test)
    
        return X_train, X_test, y_train, y_test
    
    def prepare_data_inference(self,data:np.ndarray):
        """
        Prepare data for inference

        Parameters
        ----------
        data: `numpy.ndarray`
            The data to prepare for inference
        
        Returns
        -------
        `numpy.ndarray`
            The data prepared
        """
        try:
            return self.__scaler.transform(data)
        except:
            print('Cannot infer normalisation stats from training data. Make sure you have parsed it')





        







    
