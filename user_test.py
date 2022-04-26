import unittest
from credentials import Credentials
from user import User
   
class TestUser(unittest.TestCase):
   
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Josh","brian") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Josh")
        self.assertEqual(self.new_user.user_password,"brian")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_display_all_Users(self):
        '''
        test case that test to check if we receive the list of the saved user
        '''

        self.assertEqual(User.display_user(),User.user_list)

    def test_log_in(self):
        '''
        Test case to test if a user can log into their credentials
        '''
        self.new_user.save_user()
        test_user = User("Josh","brian")
        test_user.save_user()
        self.assertEqual(User.log_in("Josh", "brian"), Credentials.credentials_list)   
        

if __name__ == '__main__':
    unittest.main()
