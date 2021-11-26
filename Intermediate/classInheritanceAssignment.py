#
#Python: 3.10.0
#
#Author: Kyle Crews
#
#Purpose: These are classes a college may use to define their student body. Every student has the general
#attributes of the student object.  Some students may also have attributes of being a college athlete or a resident
#assistant for a dormitory.

#parent class for students
class Student:
    name = 'No Name Provided'
    email = ' '
    phoneNumber = 0
    grade = 0

#child class for students who are athletes
class Athlete(Student):
    sport = ' '
    foodAllowance = 0
    scholarship = 0

#child class for students who are resident assistants
class ResidentAssistant(Student):
    boardingAllowance = 0
    scholarship = 0
    tenure = 0