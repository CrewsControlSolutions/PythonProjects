


# parent class
class Organism:
    name = 'Unknown'
    species = 'Unknown'
    legs = None
    arms = None
    dna = 'Seq A'
    origin = 'Unknown'
    carbonBased = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin {}\nCarbond Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self. origin, self.carbonBased)
        return msg

# child class instance
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapien'
    legs=2
    arms=2
    origin='Earth'

    def ingenuity(self):
        msg = '\nCreates a deadly weapon using only a paper clib, chewing gum, and a roll of duct tape.'
        return msg

# another child class instance
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Seq B'
    origin = "Earth"

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on its target."
        return msg

# another child class instance
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'Seq C'
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide, and multiply into two separate organisms."
        return msg





if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())









