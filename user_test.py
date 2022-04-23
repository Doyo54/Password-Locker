import unittest
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


if __name__ == '__main__':
    unittest.main()
