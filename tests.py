import unittest #importing unittest module
from user import User #importing the user class
from credentials import Credentials #importing the credentials class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviors.
    Args:
        unittest.TestCase:testcase class that helps in creating test cases.
    '''
    def setUp (self):
        '''
        set up method before each test case
        '''
        self.new_user = User ("james","eve") #created user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.username,"james")
        self.assertEqual(self.new_user.password,"eve")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviors.
    Args:
        unittest.TestCase:testcase class that helps in creating test cases.
    '''
    def setUp (self):
        '''
        set up method before each test case
        '''
        self.new_credentials = Credentials ("twitter","james", "eve") #created credentials object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_credentials.appname,"twitter")
        self.assertEqual(self.new_credentials.username,"james")
        self.assertEqual(self.new_credentials.password,"eve")

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("twitter","james","eve") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)


if __name__ ==  '__main__':
    unittest.main()

