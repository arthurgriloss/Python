class Bill:
    def __init__ (self, title, expense, payer_user, date, user_list):
        self.__title = title
        self.__expense = expense
        self.__payer_user = payer_user
        self.__date = date
        self.__user_list = user_list

    def getTitle(self):
        return self.__title
    
    def getExpense(self):
        return self.__expense

    def getPayerUser(self):
        return self.__payer_user

    def getDate(self):
        return self.__date
    
    def getUserList(self):
        return self.__user_list
    
    def setTitle(self, title):
        self.__title = title
    
    def setExpense(self, expense):
        self.__expense = expense
    
    def setPayerUser(self, payer_user):
        self.__payer_user = payer_user

    def setDate(self, date):
        self.__date = date
    
    def setUserList(self, user_list):
        self.__user_list = user_list

    def summary(self):
        return [self.__title, self.__expense, self.__payer_user, self.__date, self.__user_list]