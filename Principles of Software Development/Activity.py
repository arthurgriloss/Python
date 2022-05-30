class Activity:
    def __init__(self, title, description, user_list):
        self.__title = title
        self.__description = description
        self.__user_list = user_list
    
    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description

    def getUserList(self):
        return self.__user_list

    def setTitle(self, title):
        self.__title = title
    
    def setDescription(self, description):
        self.__description = description

    def setUserList(self, user_list):
        self.__user_list = user_list

    def summary(self):
        return [self.__title, self.__description, self.__user_list]
