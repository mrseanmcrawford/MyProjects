class Protected:
    def _init_(self):
        self._protectedVar = 10
        self.__privateVar = 20

    print(self.__privateVar,self._protectedVar)
