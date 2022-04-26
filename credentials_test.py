import unittest
from credentials import Credentials

class testCredentials(unittest.TestCase):
     
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Instagram", "Josh","brian") # create credentials object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.credential_name,"Instagram")
        self.assertEqual(self.new_credentials.credential_user_name,"Josh")
        self.assertEqual(self.new_credentials.credential_password,"brian")
    

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into the credentials list'
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
    unittest.main()        