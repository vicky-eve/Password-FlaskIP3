class User:
    """
    class that generates new instances of the user.
    """

    user_list = [] # Empty User list
    def __init__ (self, username,password):

        '''
        __init__ method to define properties for our user.

        Args:
            username:new_user username.
            password : new_user password.
            '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_list.
        '''
        User.user_list.append(self)