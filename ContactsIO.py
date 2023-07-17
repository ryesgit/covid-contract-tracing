import json
from utils.user_data_helpers import convert_data_to_array

class ContactsIO:
    '''
    Responsible for the delegation of the input/output of the contacts

    Parameters
    ----------
    path: str
        The path json file of the contacts
    '''
    def __init__(self, path: str):
        self.__path = path
        self.__contacts = None
        self.__read_json()

    def __read_json(self):
        '''
        Reads the json file and returns a list of dictionaries.
        '''
        with open(self.__path, 'r') as file:
            self.__contacts = json.load(file)

    def get_user_data(self):
        # Convert the data to an array first
        self.__contacts = convert_data_to_array(self.__contacts)
        return self.__contacts