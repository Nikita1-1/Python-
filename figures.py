


class Figure:#parent class

    def __init__(self, width, height, radius, color, shape):#taking parametrs from another classes via constructor
        self.width = width
        self.height = height
        self.radius = radius
        self.color = color
        self.shape = shape
        
    def print_shape(self):#method that takes parametrs from child classes and print the text based on shape
         print('this shape is: {}'.format(self.shape))

class Circle(Figure):#child class

    def __init__(self, width, height, radius, color, shape, size):#creating own parametrs that is not operating with parent class
        super().__init__(width, height, radius, color, shape)# super function is the same as if we put parent class Name, however now we no need to use SELF, because super is taking care of it

        
        self.size = size

    def calculate(self):#own method to calculate the radius
        return self.radius * self.width **2

class Rectangle(Figure):#child class

    def __init__(self, width, height, radius, color, shape, mid_line):# creating own attributes for rec class where parent class dont see it
         super().__init__(width, height, radius, color, shape)# connecting parent class that it can operate with rectangle class. 

         self.mid_line = mid_line

    def calculate(self):#own method to find volume of the rect
        return self.width * self.height



c1 = Circle(5,0, 3.14, 'Red', 'Circle', 20)# c1 as a new object is taking parametrs that inherit from parent class
c2 = Circle(9,0, 3.14, 'Orange', 'Circle', 39)
print(c1.calculate())#print object c1 with calculate method
print(c2.calculate())
print(c1.print_shape(), c2.print_shape())

r1 = Rectangle(15, 11, 0, 'Blue', 'Rectangle', 17)
print(r1.calculate())
print(r1.print_shape())

def different_forms(Figure):# polymorphism. i can create this function based on that parent class has print_shape method that both Circle &  Rectangle inherit from there
    #that means that this function is making sure that function print_shape is in child classes
    print('Let\'s see what is the shape')
    Figure.print_shape()

    shape_arr = [Circle(5,0, 3.14, 'Red', 'Circle', 20), Rectangle(15, 11, 0, 'Blue', 'Rectangle', 17)]

    for shape in shape_arr:
       return different_forms(Figure)
        



    
  
