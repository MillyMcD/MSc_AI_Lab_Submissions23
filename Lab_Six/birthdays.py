import json

class BirthdayLab:
    def __init__(self,birthdays_path):
        #using the open function to load a json file into a python dictionary
        with open(birthdays_path, 'r') as read_file:
            self.birthdays_dict = json.load(read_file)

        #creating a copy of the dictionary where all he keys are lower case using `.lower()`
        self.birthdays_dict_lower={}
        for key,value in self.birthdays_dict.items():
            self.birthdays_dict_lower[key.lower()]=value

        #loop through dictionary and print names
        print ('Welcome to the Birthday Dictionary, We know the birthdays of:')
        for name in self.birthdays_dict.keys():
            print(name)

        #get user input and check user input is in our dictionary
        #we use the `.lower()` to remove the issue of lower cases vs upper
        self.user_input=input ("Who's birthday do you want to look up? \n")
        if self.user_input.lower() not in self.birthdays_dict_lower.keys():
            print(f"The key {self.user_input} is not in my dictionary.")
            return

        #getting the birthday value using the user input and printing the result
        birthday = self.birthdays_dict_lower[self.user_input.lower()]
        print(f"{self.user_input}'s birthday is {birthday}.")

bl = BirthdayLab(birthdays_path="birthdays.json")