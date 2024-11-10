# teaching myself object oriented programming

# everything is a class
# def func():
#     print('Hi')
#
#print(type(func))

# creating a class
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

d = Dog("Tim", 34)
print(d.get_name)
d2 = Dog("Bill", 12)
print(d2.get_age)
