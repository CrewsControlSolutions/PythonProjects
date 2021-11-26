class Car:
    make = 'unknown'
    model = 'unknown'
    year = None
    color = 'unknown'

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color




class Maintenance(Car):
    oilType = 'unknown'
    oilChangeFrequency = 'unknown'

    def __init__(self, oilType, oilChangeFrequency):
        self.oilType = oilType
        self.oilChangeFrequency = oilChangeFrequency


if __name__ == "__main__":
    myCar = Car('Toyota', None, 1997, None)
    print(myCar.make, myCar.model, myCar.year, myCar.color)

    myCarMaintenance = Maintenance('full synthetic', '12 months')
    print(myCarMaintenance.oilType, myCarMaintenance.oilChangeFrequency,myCarMaintenance.make,myCar.make)
