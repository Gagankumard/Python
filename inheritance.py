class Mammels:
    def walk(self):
        print("Dog Walk")


class Dog(Mammels):
    def bark(self):
        print("Dog Bark")


class Cat(Mammels):
    def cute(self):
        print("Cuteee..!")


dog1=Dog()
dog1.walk()
dog1.bark()
cat1=Cat()
cat1.cute()
