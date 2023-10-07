import json

class BirthdayLab:
    def __init__(self,birthdays_path):
        with open(birthdays_path, 'r') as read_file:
            self.birthdays_dict = json.load(read_file)

        self.birthdays_dict_lower={}
        for key,value in self.birthdays_dict.items():
            self.birthdays_dict_lower[key.lower()]=value

        print ('Welcome to the Birthday Dictionary, We know the birthdays of:')

        for name in self.birthdays_dict.keys():
            print(name)

        self.user_input=input ("Who's birthday do you want to look up? \n")
        if self.user_input.lower() not in self.birthdays_dict_lower.keys():
            print(f"The key {self.user_input} is not in my dictionary.")
            return

        birthday = self.birthdays_dict_lower[self.user_input.lower()]
        print(f"{self.user_input}'s birthday is {birthday}.")

bl = BirthdayLab(birthdays_path="birthdays.json")