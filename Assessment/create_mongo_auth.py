import pymongo
import pandas as pd


class ConstructAuthDB():
    """
    ConstructAuthDB. Class to instantiate and load the csv into mongodb, before creating a user.
    """
    def __init__(self):
        #create a mongo client
        self.__client = pymongo.MongoClient()

        #create a database to store the data
        self.__db = self.__client['pulsar_database']

        #this collection stores the raw dataset
        self.__col = self.__db['raw_data']

    def insert_records(self,path_to_dataset):
        """
        Insert records into mongodb collection

        Parameters
        ----------
        path_to_dataset : `str`
            A path to the dataset
        """
        
        #using pandas to read the file as a dataframe
        df = pd.read_csv(path_to_dataset)
        #convert each row in the dataset to a dictionary record
        records = df.to_dict(orient='records')
        #inserting the records into our collection
        self.__col.insert_many(records)

        rec_count = self.__col.count_documents({})
        print(f'{rec_count} inserted into raw_data.collection of pulsar_database')

    def create_user(self,name,password):
        """
        Create a username and password for the collection/database

        Parameters
        ----------
        name : `str`
            the username
        password : `str`
            the password
        """
        self.__db.command('createUser', name, pwd=password, roles=['readWrite'])
        print(f'Created auth for {name}')

    def teardown(self):
        """
        close the client
        """
        self.__client.close()


if __name__ == "__main__":
    #get credentials
    name = input('Please provide a username:\n')
    password = input('Please provide a password:\n')

    #create instance
    cadb = ConstructAuthDB()

    #insert the dataset
    cadb.insert_records('PulsarDataset.csv')

    #create a user
    cadb.create_user(name,password)

    #teardown instance
    cadb.teardown()