# Implement encapsulation by creating a protected or private method
class Protected:
    def __init__(self):
        self._protectedVar = 0 # Protected prefixed with single underscore "_". Tells other developers that "this is protected"
        self.__privateVar = 22 # Private prefixed with double underscore "__"

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private


obj = Protected()
obj._protectedVar = 83
print(obj._protectedVar)

# Obj gets the data of the private variable. We set the privateVar
# with a new value and then ask for it to be retrieved
obj.getPrivate()
obj.setPrivate(45)
obj.getPrivate()
