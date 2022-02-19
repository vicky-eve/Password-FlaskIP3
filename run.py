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

#credentials methods
def create_credentials(appname,username, password):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(appname,username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save new credentials
    '''
    credentials.save_credentials()

def display_all_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_all_credentials()

def del_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()