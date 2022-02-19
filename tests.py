import unittest #importing unittest module
from user import User #importing the user class

class TestUser(unittest.TestCase)
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
