import string
import random
class Credentials:
    credentials_list=[] #empty list of credentials

    def __init__(self, credential_name,credential_user_name, credential_password):
        '''
        __init__ method to define the properties of a Credentials object
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
        delete_cred method deletes a saved credential from the credentials_list
        '''
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def display_cred(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list       

    @classmethod
    def generate_password(cls):
        '''
        Method that generates a random alphanumeric password
        '''

        length = 10
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase + "!@#$%^&*" 
        password = ''.join( random.choice(alphanum) for num in range(length) )
        
        return password  
    @classmethod
    def find_Credential(cls,credential_name):
        '''
        Method that takes in a credential name and returns a credentials that matches that name.
        '''

        for credentials in cls.credentials_list:
            if credentials.credential_name == credential_name:
                return credentials         