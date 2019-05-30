class Animal:
    origin = "I am an animal from the animal kingdom on earth"
    # Class - blueprint of an object
    # Define how it looks (method__init__)
    # Define how it behaves (methods)

    def __init__(self, species, colour= '', loc = ''):
        self.species = ''
        self.alive = True
        self.colour = ''
        self.location = ''
        self.eyes = True
        self.lungs = True

    # Behaviour (method)
    def sleep(self):
        print('so sleeeeeppppiiiinnnngggg')

    def breath(self):
        print('inhalllleee......exhalll;le')

    def eat(self, food = ''):
        print('nom nom',food)

    def potty(self):
        print("0.0....0.o! uhhh.... PLOP")

    def what_are_you(self):
        # self refers to the instance of Animal class. NOT the class
        print(self.origin)

# To call the method we need an animal object
# Initiate an animal object

dogo = Animal('Dogo')

# Now that you have an animal object
dogo.breath()
dogo.eat()
dogo.potty()
dogo.sleep()

dogo.what_are_you()
