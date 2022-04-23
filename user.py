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
