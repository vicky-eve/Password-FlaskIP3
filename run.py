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

def main():
    print("Oh Hello There! Welcome to the Password app! Where you get to save your secrets")
    username = input ("Enter your username")

    while True:
        print(f"Hi there {username}, use either of these codes to sign or log in")
        print("sn - sign up to new users")
        print("lg - log into your account")
        short_code = input("Enter short code:").upper()

        if short_code == 'SN':
            print("Enter yout username: ")
            username = input()

            print("Enter your desired password")
            fpin = input()
            print('*' * 60)

            print("Successful registration!")
            print("Now log into your account",)
            print('\n')

        elif short_code == 'LG':
            print("Enter your username")
            username = input()

            print("Enter your password")
            password= input()
            if f"{username } = {password}":
                print('*' * 10)

                print(f"{username}, you've succesfully logged into your account")
                print('\n')

                pass