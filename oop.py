





# parent class
class Organizm:
    name = 'Unknown'
    species = 'Unknown'
    legs = None
    arms = None
    dna = 'Sequence A'
    iq = None
    origin = 'Unknown'
    carbon_based = True
    
    def Information(self):
        msg = '\nName: {} \nSpecies: {}\nLegs: {} \nArms: {} \nDNA: {} \nIQ: {} \nOrdigin: {} \nCarbon_based:{}'.format(self.name, self.species, self.legs, self.arms, self.dna, self.iq, self.origin, self.carbon_based)
        return msg


class Human(Organizm):
    name = 'Marty McFly'
    species = 'Homosapiens'
    legs = 2
    arms = 2
    origin = 'Earth'

    def Information(self):
        msg = '\nName: {} \nSpecies: {}\nLegs: {} \nArms: {} \nOrdigin: {}'.format(self.name, self.species, self.legs, self.arms, self.origin)
        return msg

class Dog(Organizm):
    name = 'Copernicus'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Squence C'
    origin = 'Earth'
    carbon_based = 'yes'

    def Information(self):
        msg = '\nName: {} \nSpecies: {}\nLegs: {} \nArms: {} \nDNA: {} \nOrdigin: {} \nCarbon_based:{}'.format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg


class Genius(Organizm):
    name ='Doc Brown'
    species = 'Homosapiens'
    legs = 2
    arms = 2
    iq = 300

    def Information(self):
        msg = '\nName: {} \nSpecies: {}\nLegs: {} \nArms: {} \nIQ: {}'.format(self.name, self.species, self.legs, self.arms, self.iq)
        return msg




if __name__=='__main__':
    Human = Human()
    print(Human.Information())

    Dog = Dog()
    print(Dog.Information())

    Genius = Genius()
    print(Genius.Information())












    
