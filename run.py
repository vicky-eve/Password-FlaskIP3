#!/usr/bin/env python3
from user import User #importing the user class
from credentials import Credentials #importing credentials class

#user methods
def create_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save new user
    '''
    user.save_user()

