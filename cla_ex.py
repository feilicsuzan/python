class organism(object):
    def __init__(self):
        self.cell=True
class animal(organism):
    def __init__(self):
        super(animal,self).__init__()
        self.move=True
class vertbrate(animal):
   def __init__(self):
        super(vertbrate,self).__init__()
        self.bony=True
class mammal(vertbrate):
    def __init__(self):
        super(mammal,self).__init__()
        self.milk=True
class dog(mammal):
     def __init__(self):
        super(dog,self).__init__()
        self.bark=True
