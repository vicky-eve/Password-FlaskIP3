import unittest #importing unittest module
from user import User #importing the user class

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


if __name__ ==  '__main__':
    unittest.main()

