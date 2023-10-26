import pymongo
import pandas as pd

class DatabaseClient:
    """
    DatabaseClient class. Connects to MongoDB and provides a method to talk grab
    records from the database

    Parameters
    ----------
    username : `str`
        Your username
    password: `str`
        The password
    dbname : `str`
        The name of the database
    """
    def __init__(self,username:str,password:str,dbname:str):
        self.login(username,password,dbname)
        if self.__client is not None:
            self.__db = self.__client[dbname]  
        else:
            print('Client not available, check credentials.')

    def login(self,username:str,password:str,dbname:str):
        """
        Login function. Checks credentials match the mongo database
        
        Parameters
        ----------
        username : `str`
            Your username
        password: `str`
            The password
        dbname : `str`
            The name of the database
        """
        #creating a pymongo client to talk to my database
        self.__client= pymongo.MongoClient(
            username = username,
            password = password,
            authSource = dbname,
            authMechanism = 'SCRAM-SHA-256')
        #checking I can list the database names to check its logged in properly
        try:
            self.__client.list_database_names()
            print('Successful login')
        #if it failed I set the client = None
        except:
            print('Login failed')
            self.__client = None

    def get_all_records(self,collection:str,as_df:bool=False):
        """
        Get all records from a collection in the database

        Parameters
        ----------
        collection : `str`
            The collection name to grab records from
        as_df : `bool`, optional
            bool. Returns a DataFrame if true, else returns a list of records
        
        Returns
        --------
        `list` or `pandas.DataFrame`
            The records as a list or DataFrame
        """
        #check if collection is in the database
        if collection in self.__db.list_collection_names():
            #find all records
            records = list(self.__db[collection].find({}))

            #if DataFrame, convert records to df and drop _id column
            if as_df:
                df = pd.DataFrame(records)
                df.drop(columns='_id',inplace=True)
                return df
            else:
                return records
        else:
            print(f'Collection "{collection}" not found in database. Please insert records')
    
    def insert_records(self,collection:str,records:list):
        """
        Insert records into a collection

        Parameters
        ----------
        collection : `str`,
            The collection name
        records: `list`
            Records to insert
        """
        self.__db[collection].insert_many(records)
    
    def is_logged_in(self):
        """Shows if database is logged in or not
        
        Returns
        -------
        `bool`
            True if logged in
        """
        return self.__client is not None
    
    def get_database(self):
        """
        Return the database

        Returns
        -------
        MongoClient database
        """
        return self.__db

    def get_client(self):
        """
        Return the client

        Returns
        -------
        MongoClient database
        """
        return self.__client

    def teardown(self):
        """"
        teardown the client
        """
        self.__client.close()


def add_new_user(client:DatabaseClient,username,password):
    """
    Give a new user database credentials

    Parameters
    ----------
    client : `DatabaseClient`
        The database client instance
    username : `str`
        Your username
    password: `str`
        The password
    """
    db = client.get_database()
    db.command('createUser', username, pwd=password, roles=['readWrite'])
    print(f'Created user {username}')



        