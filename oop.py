





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
    name = 'McFly'
    species = 'Homosapiens'
    legs = 2
    arms = 2
    origin = 'Earth'

    def genius(self):
        msg = 'Traveled Back To The Future Via Doc Brown and DeLorean'
        return msg

class Dog(Organizm):
    name = 'Copernicus'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Squence C'
    origin = 'Earth'
    carbon_based = 'yes'

    def travel_dog(self):
        msg = 'Very lazy and smart dog of Doc Brown who traveld to the future and back in time'
        return msg


class Genius(Organizm):
    name ='Doc Brown'
    species = 'Homosapiens'
    legs = 2
    arms = 2
    iq = 300

    def time_machine(self):
        msg = 'Ginius Guy Made Time Machine from DeLorean and then from a Train'
        return msg
    
        












if __name__=='__main__':
    Human = Human()
    print(Human.Information())
    print(Human.genius())

    Dog = Dog()
    print(Dog.Information())
    print(Dog.travel_dog())

    Genius = Genius()
    print(Genius.Information())
    print(Genius.time_machine())












    
