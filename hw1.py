#multilevel inheritance

class Grandfather:
    land = ''

    def __init__(self,l):
        self.land = l

    def show_property(self):
        print("Grandfather has: ", self.land)

class Parent(Grandfather):
    def __init__(self, l, h):
        super().__init__(l)
        self.house = h

    def show_property(self):
        super().show_property()
        print("Parent has: ", self.house)

class Child(Parent):
    def __init__(self, l, h, c):
        super().__init__(l, h)
        self.car = c
    
    def show_property(self):
        super().show_property()
        print("Child has: ", self.car)

c1 = Child("5 bigha", "two apartments", "a new car")

land = input("Enter how much land your grandfather has: ")
house = input("Enter what house your parent has: ")
car = input("Enter what car you have: ")
c1 = Child(land, house, car)

print()
c1.show_property()
