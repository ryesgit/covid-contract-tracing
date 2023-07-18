import json
from utils.user_data_helpers import convert_data_to_array
from uuid import uuid4

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
        try:
            with open(self.__path, 'r') as file:
                self.__contacts = json.load(file)
        except:
            self.__contacts = {}
    def get_user_data(self):
        # Convert the data to an array first
        self.__contacts = convert_data_to_array(self.__contacts)
        return self.__contacts

    def write_user_data(self, user_data: dict):
        '''
        Writes the user data to the json file.

        Parameters
        ----------
        user_data : dict
            The user data to write to the json file.
        '''

        # Generate a unique id for the user
        id = str(uuid4())
        
        self.__contacts[id] = user_data
        with open(self.__path, 'w') as file:
            json.dump(self.__contacts, file, indent=4)