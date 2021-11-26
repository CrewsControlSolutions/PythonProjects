#
# Python: 3.10.0
#
# Author: Kyle Crews
#
# Purpose: A demonstration of parent and child classes as well as polymorphism among the child classes. The specific use case is a hypothetical car dealership interested in tracking and advertising their vehicles for sale, as well as the specific maintenance and tires for a given vehicle.


class Car:
    """requires a make, model, year, and color, in that order"""
    make = 'unknown'
    model = 'unknown'
    year = None
    color = 'unknown'

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # this method is used to provide an advertisement to an electronic display for a specific car at the dealership
    def advertisement(self):
        """produces an advertisement for a specific vehicle"""
        msg = "Come by our dealership and purchase a {} {} {} today!".format(self.year, self.make, self.model)
        return msg

# required maintenance for a specific type of car
class Maintenance(Car):
    oilType = 'unknown'
    oilChangeFrequency = 'unknown'

    def __init__(self, oilType, oilChangeFrequency):
        self.oilType = oilType
        self.oilChangeFrequency = oilChangeFrequency

    # this method is an example of polymorphism since the parent class has a function named the same. the goal of this method is to provide an advertisement for maintenance on a customer's specific type of car.
    def advertisement(self):
        msg = "Your vehicle needs a {} oil change every {}, so be sure to stop by our on-site auto shop today.".format(self.oilType, self.oilChangeFrequency)
        return msg


class Tires(Car):
    allTerrain = False
    rimSize = None
    brand = 'unknown'

    def __init__(self, allTerrain, rimSize, brand):
        self.allTerrain = allTerrain
        self.rimSize = rimSize
        self.brand = brand

# a polymorphed method used to provide an advertisement for a customer's specific tires for their vehicle
    def advertisement(self):
        msg = "Your vehicle needs tires with a rim size of {} and preferably the {} brand, so stop by our on-site tire center today.".format(self.rimSize, self.brand)
        return msg

# assign values to all of the attributes from all of the classes in this Python script
if __name__ == "__main__":
    myCar = Car('Toyota', 'Camery', 1997, 'Silver')
    print(myCar.make, myCar.model, myCar.year, myCar.color)
    print(myCar.advertisement()+"\n")

    myCarMaintenance = Maintenance('full synthetic', '12 months')
    print(myCarMaintenance.oilType, myCarMaintenance.oilChangeFrequency)
    print(myCarMaintenance.advertisement()+"\n")

    myCarTires = Tires(False, '26.5"',"Bridgestone")
    print(myCarTires.allTerrain, myCarTires.rimSize, myCarTires.brand)
    print(myCarTires.advertisement()+"\n")