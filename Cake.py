

class Cake:
    def __init__(self, size, flavor, color):
        self.size = size
        self.flavor = flavor
        self.color = color
    def print_cake(self):
        print('Cake Size: {}, \nCake Flavor: {}, \nCake Color: {}\n'.format(self.size, self.flavor, self.color))


Red_Velvet = Cake('12', 'Red Velvet', 'Red')
Honey_Comb = Cake('10', 'Honey', 'Yellow')


Red_Velvet.print_cake()
Honey_Comb.print_cake()



class Vehicle:
    make = 'Unknown'
    model = 'Unknown'
    engine = 'Diesel'
    year = None
    color = 'Blue'

class Jeep:(Vehicle):
    make = 'Jeep'
    model = 'Grand Wagooner'
    engine = 'Gasoline'
    year = 2022
    color = 'night sky'
    
