class User:
    """
    class that generates new instances of the user.
    """

    user_list = [] # Empty User list
    def __init__ (self, username,password):

        '''
        __init__ method to define properties for our methods.

        Args:
            username:new_user username.
            password : new_user password.
            '''
        self.username = username
        self.password = password