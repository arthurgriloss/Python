class User:
    def __init__(self, user, password):
        self.__user = user
        self.__password = password

    def getUser(self):
        return self.__user

    def getPassword(self):
        return self.__password

    def setUser(self, user):
        self.__user = user
    
    def setPassword(self, password):
        self.__password = password

    def summary(self):
        return [self.__user, self.__password]