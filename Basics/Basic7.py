# 
# Python: _._._
# 
# Author: Kyle Crews
# 
# Purpose: A demonstration of how to pass variables from function to function.

def start():
    fName = "Sarah"
    lName = "Thompson"
    age = 88
    gender = "female"
    getInfo(fName, lName, age, gender)


def getInfo(fName, lName, age, gender):
    print("My name is {} {}. I am a {} year old {}.".format(fName, lName, age, gender))



if __name__ == "__main__":
    start()
