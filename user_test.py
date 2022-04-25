import unittest
from credentials import Credentials
from user import User
   
class TestUser(unittest.TestCase):
   
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Muriuki") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"James")
        self.assertEqual(self.new_user.user_password,"Muriuki")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

if __name__ == '__main__':
    unittest.main()
