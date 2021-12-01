#
# Python Ver:   3.10.0
#
# Author:   Kyle M. Crews
#
# Purpose: The class registration date for a college student when he registers for classes are specific to that
# student. This file attempts to replicate this basic back-end functionality with two classes--one for students and
# the other for students of a specific grade. This file also demonstrates the use of parent and child classes,
# as well as abstract methods.
#
# Tested OS: This code was written and tested to work with Mac OSX.
#

# import the Abstract Base Class (ABC) and abstractmethod methods from 'abc'
from abc import ABC, abstractmethod
class student(ABC):
    """This class contains two methods that require a passed student name. The class is for students of all grades."""
    def registrationWelcome(self, name):
        print("Welcome to the Tennessee School of Computer Science, "+name+". Please use this portal to register for "
                                                                           "classes.")
    # define an abstract method since the seniority of the student is not known within this class
    @abstractmethod
    def registrationDate(self, name):
        pass


# a generic registration date statement
class sophomore(student):
    """This class is for sophomores registering for classes. Its method requires that the student name be passed."""
    # define the implementation of the abstract method inherited from the parent class
    def registrationDate(self, name):
        date = 'April 18'
        print(name+", because you are a sophomore by credit level, your class registration date is "+date+".")

# create an object that is an instance of the 'sophomore' class
student49200 = sophomore()
# utilize a method from the parent class 'student' and pass a student name to this method
student49200.registrationWelcome("Chris Collins")
# utilize a method from the child class 'sophomore' and pass a student name to this method
student49200.registrationDate("Chris Collins")