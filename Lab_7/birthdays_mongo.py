#Lab 7, recreating the birthdays.py in python using a MongoDB script
import pymongo

#defining a class, running the arguments database and collection
class BirthdayMongo:
    def __init__(self,database_name,collection_name):
        #creating a client, then getting the database and collection
        self.client=pymongo.MongoClient()
        self.db=self.client[database_name]
        self.collection=self.db[collection_name]
        
        #getting all birthdays using a find query
        self.allentries=self.collection.find({})
        print('We have the Birthdays for ')
        for doc in self.allentries:
            print(doc['name'])

        #creating a query for a specific birthday and printing result
        self.user_input=input ("Who's birthday do you want to look up? \n")
        query = {'name':self.user_input}
        results = list(self.collection.find(query))
        for result in results:
            print(f"{self.user_input}'s birthday is {result['dob']}")

        #if imput isn't in the collection, return this string
        if len(results) <1:
            print('This name is not in the database, please try again or check your spelling')

#running the code, calling an instance of the class
bm=BirthdayMongo(database_name='BirthdayDatabase',collection_name='Birthdays')


