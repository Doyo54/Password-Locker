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