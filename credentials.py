class Credentials:
    """
    class that generates new instances of credentials.
    """
    credentials_list = [] #empty credentials list
    def __init__ (self, appname, username,password):
        '''
        __init__ method to define properties of our user.
        Args:
            appname:new_credentials appname.
            username : new_credentials username.
            password : new_credentials password.
            '''
        self.appname = appname
        self.username = username
        self.password = password

    def save_credentials (self):
        '''
        save_credentials method saves credentials objects into credentials_list.
        '''
        Credentials.credentials_list.append(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credential from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

       
