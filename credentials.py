import string
import random
class Credentials:
    credentials_list=[] #empty list of credentials

    def __init__(self, credential_name,credential_user_name, credential_password):
        '''
        __init__ method to define the properties of a User object
        '''
        self.credential_name = credential_name
        self.credential_user_name = credential_user_name
        self.credential_password = credential_password

    def save_credentials(self):
        '''
        Method that saves a user's credentials to credential list
        '''
        Credentials.credentials_list.append(self)
    
    def delete_cred(self):
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''
        Credentials.credentials_list.remove(self)
    

    @classmethod
    def display_cred(cls):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list       

    @classmethod
    def generate_password(cls):
        '''
        Method that generates a random alphanumeric password
        '''

        size = 8
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase + "!@#$%^&*()"

        # Create password
        password = ''.join( random.choice(alphanum) for num in range(size) )
        
        return password  
    @classmethod
    def find_Credential(cls,credential_name):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for credentials in cls.credentials_list:
            if credentials.credential_name == credential_name:
                return credentials         