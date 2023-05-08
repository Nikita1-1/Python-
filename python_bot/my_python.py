class Organizm:
	name = ''
	species = ''
	arms = None
	iq = None

	def info(self):
		msg = '\nFirst_Name: {}, \nSpecies: {}, \narms: {}, \niq: {}'.format(self.name, self.species, self.arms, self.iq)
		return msg

class Human(Organizm):
	name = 'Nikita'
	species = 'Human'
	arms = 4
	iq = 120

	# def info(self):
	# 	msg = '\nName: {}, \nSpecies: {}, \narms: {}, \niq: {}'.format(self.name, self.species, self.arms, self.iq)
	# 	return msg

if __name__ == '__main__':
	human = Human()
	print(human.info())

def countOdds(low: int, high: int) -> int:
    numb = []
    if low % 2 != 0:
        numb.append(low)
    if high % 2 != 0:
        numb.append(high)
    diff = high - low 
    for num in range(low), diff:
    	print(num)
        # if num % 2 != 0:
        #     numb.append(num)
        #     print(numb)
    print(numb)

countOdds(3, 7)
       