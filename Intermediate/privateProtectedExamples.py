# this class contains both a protected and a private attribute
class Beetles:
    # initialize the protected and private attributes
    def __init__(self):
        self._largeBeetle = 'Rhinocerous Beetle'
        self.__smallBeetle = 'Stag Beetle'

    # provide a way to print the private attribute
    def getPrivate(self):
        print(self.__smallBeetle)

    # provide a way to change the private attribute
    def setPrivate(self, private):
        self.__smallBeetle = private


# define an object "a" as an instance of the Beetles class
a = Beetles()
# change the value of a protected attribute
a._largeBeetle = 'Rhinoceros Beetle'
# print the value of the protected attribute
print(a._largeBeetle)

# call on the function that prints a private attribute
a.getPrivate()
# call on the function that changes a private attribute
a.setPrivate('Lady Beetle')
# call on the function that prints a private attribute. note that the private attribute has changed value since the
# last time this function was called
a.getPrivate()

