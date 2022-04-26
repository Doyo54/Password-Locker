from credentials import Credentials

class User:
    '''
    Class that generates instances of user accounts
    '''

    # Empty list of users
    user_list = []

    def __init__(self, user_name, user_password):

        #__init__ method to define the properties for our objects

        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        '''
        method that returns the User list
        '''
        return cls.user_list    

    @classmethod
    def log_in(cls, name, password):
        '''
        Method that allows a user to log into their credential
        '''

        for user in cls.user_list:
            if user.user_name == name and user.user_password == password:
                return Credentials.credentials_list

        return False
