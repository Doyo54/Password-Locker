class Credentials:
    credentials_list=[] #empty list of credentials

    def __init__(self, credential_name, credential_password):
        '''
        __init__ method to define the properties of a User object
        '''
    
        self.credential_name = credential_name
        self.credential_password = credential_password

    def save_credential(self):
        '''
        Method that saves a user's credentials to credential list
        '''
        Credentials.credentials_list.append(self)