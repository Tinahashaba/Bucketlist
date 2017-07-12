class Application:
    users = {}

    def register(self, user):
        """
        if user doesnot exist already, it creates a new use
        :param user:
        :return:
        """
        if user.email not in self.users.keys():
            self.users[user.email] = user
            return True
        return False

    def log_in(self, email, password):
        """
        checks if the password entered matches the password entered
        :param email:
        :param password:
        :return:
        """
        if email in self.users:
            return self.users[email].password == password
        return False
