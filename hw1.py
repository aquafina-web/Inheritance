#single inheritance
#problem 1
#parent class
class Person:
    name = ''
    age = ''

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show_person_info(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")

# p1 = Person('momo', 123)
# p1.show_person_info()

#child class
class Student(Person):  
    # Student_id = ''
    def display(self):
        print(f"hello, i am a child class")

# s1 = Student('mim', 12)
# s1.display()
# s1.show_person_info()
