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
