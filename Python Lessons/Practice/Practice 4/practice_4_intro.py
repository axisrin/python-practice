# Delayem class
class Animal:

    num = 10

    def __init__(self, age, name):
        self.__age = age
        self.name = name

    @classmethod
    def change_num(cls, age):
        cls.num = age

    @classmethod
    def change_num_object(self, num):
        self.num = 5

    @staticmethod
    def sum(a,b):
        return (a + b)

cat = Animal(9, 'Barsik')
dog = Animal(5, 'Bobik')

Animal.change_num(9)

print(cat.name)
print(Animal.num)

