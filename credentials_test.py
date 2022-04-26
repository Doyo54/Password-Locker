from curses.ascii import CR
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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_delete_cred(self):
        '''
        test_delete_cred to test if we can remove a credentials from our credential list
        '''
        self.new_credentials.save_credentials()
        test_cred = Credentials("Youtube","Doyo","12345") # new credentials
        test_cred.save_credentials()

        self.new_credentials.delete_cred()# Deleting a credential object
        self.assertEqual(len(Credentials.credentials_list),1)    
    

    def test_display_credentials(self):
        '''
        test case that test to check if we receive the list of the saved credential
        '''

        self.assertEqual(Credentials.display_cred(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()        